import pathlib
import pytest

from click.testing import CliRunner

from gbintk.cli import visualise


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


def test_visualise_run(runner, tmp_dir):
    outpath = tmp_dir
    initial = DATADIR / "5G_metaSPAdes" / "metacoag_res.csv"
    final = DATADIR / "5G_metaSPAdes" / "graphbin_res.csv"
    graph = DATADIR / "5G_metaSPAdes" / "assembly_graph_with_scaffolds.gfa"
    paths = DATADIR / "5G_metaSPAdes" / "contigs.paths"
    args = f"--assembler spades --initial {initial} --final {final} --graph {graph} --paths {paths} --output {outpath}".split()
    r = runner.invoke(visualise, args, catch_exceptions=False)
    assert r.exit_code == 0, r.output

def test_visualise_prefix(runner, tmp_dir):
    outpath = tmp_dir
    initial = DATADIR / "5G_metaSPAdes" / "metacoag_res.csv"
    final = DATADIR / "5G_metaSPAdes" / "graphbin_res.csv"
    graph = DATADIR / "5G_metaSPAdes" / "assembly_graph_with_scaffolds.gfa"
    paths = DATADIR / "5G_metaSPAdes" / "contigs.paths"
    args = f"--assembler spades --initial {initial} --final {final} --graph {graph} --paths {paths} --prefix test --output {outpath}".split()
    r = runner.invoke(visualise, args, catch_exceptions=False)
    assert r.exit_code == 0, r.output

def test_visualise_imgtype(runner, tmp_dir):
    outpath = tmp_dir
    initial = DATADIR / "5G_metaSPAdes" / "metacoag_res.csv"
    final = DATADIR / "5G_metaSPAdes" / "graphbin_res.csv"
    graph = DATADIR / "5G_metaSPAdes" / "assembly_graph_with_scaffolds.gfa"
    paths = DATADIR / "5G_metaSPAdes" / "contigs.paths"
    args = f"--assembler spades --initial {initial} --final {final} --graph {graph} --paths {paths} --imgtype svg --output {outpath}".split()
    r = runner.invoke(visualise, args, catch_exceptions=False)
    assert r.exit_code == 0, r.output

def test_visualise_outdir(runner, tmp_dir):
    outpath = tmp_dir / "testing"
    initial = DATADIR / "5G_metaSPAdes" / "metacoag_res.csv"
    final = DATADIR / "5G_metaSPAdes" / "graphbin_res.csv"
    graph = DATADIR / "5G_metaSPAdes" / "assembly_graph_with_scaffolds.gfa"
    paths = DATADIR / "5G_metaSPAdes" / "contigs.paths"
    args = f"--assembler spades --initial {initial} --final {final} --graph {graph} --paths {paths} --output {outpath}".split()
    r = runner.invoke(visualise, args, catch_exceptions=False)
    assert r.exit_code == 0, r.output