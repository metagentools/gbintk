import pathlib
import pytest

from click.testing import CliRunner

from gbintk.cli import graphbin, graphbin2, metacoag, visualise


__author__ = "Vijini Mallawaarachchi"
__credits__ = ["Vijini Mallawaarachchi"]


DATADIR = pathlib.Path(__file__).parent / "data"

@pytest.fixture(scope="session")
def tmp_dir(tmpdir_factory):
    return tmpdir_factory.mktemp("tmp")


@pytest.fixture(autouse=True)
def workingdir(tmp_dir, monkeypatch):
    """set the working directory for all tests"""
    monkeypatch.chdir(tmp_dir)


@pytest.fixture(scope="session")
def runner():
    """exportrc works correctly."""
    return CliRunner()


def test_graphbin_run(runner, tmp_dir):
    outpath = tmp_dir
    graph = DATADIR / "ESC_metaSPAdes" / "assembly_graph_with_scaffolds.gfa"
    contigs = DATADIR / "ESC_metaSPAdes" / "contigs.fasta"
    paths = DATADIR / "ESC_metaSPAdes" / "contigs.paths"
    binned = DATADIR / "ESC_metaSPAdes" / "initial_binning_res.csv"
    args = f"--assembler spades --graph {graph} --contigs {contigs} --paths {paths} --binned {binned} --output {outpath}".split()
    r = runner.invoke(graphbin, args, catch_exceptions=False)
    assert r.exit_code == 0, r.output

def test_graphbin2_run(runner, tmp_dir):
    outpath = tmp_dir
    graph = DATADIR / "Sim-5G+metaSPAdes" / "assembly_graph_with_scaffolds.gfa"
    contigs = DATADIR / "Sim-5G+metaSPAdes" / "contigs.fasta"
    paths = DATADIR / "Sim-5G+metaSPAdes" / "contigs.paths"
    binned = DATADIR / "Sim-5G+metaSPAdes" / "initial_contig_bins.csv"
    abundance = DATADIR / "Sim-5G+metaSPAdes" / "abundance.abund"
    args = f"--assembler spades --graph {graph} --contigs {contigs} --paths {paths} --binned {binned} --abundance {abundance} --output {outpath}".split()
    r = runner.invoke(graphbin2, args, catch_exceptions=False)
    assert r.exit_code == 0, r.output

def test_metacoag_run(runner, tmp_dir):
    outpath = tmp_dir
    graph = DATADIR / "Sim-5G+metaSPAdes" / "assembly_graph_with_scaffolds.gfa"
    contigs = DATADIR / "Sim-5G+metaSPAdes" / "contigs.fasta"
    paths = DATADIR / "Sim-5G+metaSPAdes" / "contigs.paths"
    abundance = DATADIR / "Sim-5G+metaSPAdes" / "coverm_mean_coverage.tsv"
    args = f"--assembler spades --graph {graph} --contigs {contigs} --paths {paths} --abundance {abundance} --output {outpath}".split()
    r = runner.invoke(metacoag, args, catch_exceptions=False)
    assert r.exit_code == 0, r.output

def test_visualise_run(runner, tmp_dir):
    outpath = tmp_dir
    initial = DATADIR / "Sim-5G+metaSPAdes" / "metacoag_res.csv"
    final = DATADIR / "Sim-5G+metaSPAdes" / "graphbin_res.csv"
    graph = DATADIR / "Sim-5G+metaSPAdes" / "assembly_graph_with_scaffolds.gfa"
    paths = DATADIR / "Sim-5G+metaSPAdes" / "contigs.paths"
    args = f"--assembler spades --initial {initial} --final {final} --graph {graph} --paths {paths} --output {outpath}".split()
    r = runner.invoke(visualise, args, catch_exceptions=False)
    assert r.exit_code == 0, r.output

def test_visualise_prefix(runner, tmp_dir):
    outpath = tmp_dir
    initial = DATADIR / "Sim-5G+metaSPAdes" / "metacoag_res.csv"
    final = DATADIR / "Sim-5G+metaSPAdes" / "graphbin_res.csv"
    graph = DATADIR / "Sim-5G+metaSPAdes" / "assembly_graph_with_scaffolds.gfa"
    paths = DATADIR / "Sim-5G+metaSPAdes" / "contigs.paths"
    args = f"--assembler spades --initial {initial} --final {final} --graph {graph} --paths {paths} --prefix test --output {outpath}".split()
    r = runner.invoke(visualise, args, catch_exceptions=False)
    assert r.exit_code == 0, r.output

def test_visualise_imgtype(runner, tmp_dir):
    outpath = tmp_dir
    initial = DATADIR / "Sim-5G+metaSPAdes" / "metacoag_res.csv"
    final = DATADIR / "Sim-5G+metaSPAdes" / "graphbin_res.csv"
    graph = DATADIR / "Sim-5G+metaSPAdes" / "assembly_graph_with_scaffolds.gfa"
    paths = DATADIR / "Sim-5G+metaSPAdes" / "contigs.paths"
    args = f"--assembler spades --initial {initial} --final {final} --graph {graph} --paths {paths} --imgtype svg --output {outpath}".split()
    r = runner.invoke(visualise, args, catch_exceptions=False)
    assert r.exit_code == 0, r.output

def test_visualise_outdir(runner, tmp_dir):
    outpath = tmp_dir / "testing"
    initial = DATADIR / "Sim-5G+metaSPAdes" / "metacoag_res.csv"
    final = DATADIR / "Sim-5G+metaSPAdes" / "graphbin_res.csv"
    graph = DATADIR / "Sim-5G+metaSPAdes" / "assembly_graph_with_scaffolds.gfa"
    paths = DATADIR / "Sim-5G+metaSPAdes" / "contigs.paths"
    args = f"--assembler spades --initial {initial} --final {final} --graph {graph} --paths {paths} --output {outpath}".split()
    r = runner.invoke(visualise, args, catch_exceptions=False)
    assert r.exit_code == 0, r.output