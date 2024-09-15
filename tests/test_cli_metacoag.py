import os
import pathlib

import pytest
from click.testing import CliRunner

from gbintk.cli import metacoag

__author__ = "Vijini Mallawaarachchi"
__credits__ = ["Vijini Mallawaarachchi"]


DATADIR = pathlib.Path(__file__).parent / "data"


@pytest.fixture(scope="function")
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


def get_files_and_seq_counts(output_path):
    output_files = os.listdir(output_path)
    seq_counts = []
    for file in output_files:
        seq_count = 0
        with open(f"{output_path}/{file}", "r") as myfile:
            for line in myfile:
                if line.strip().startswith(">"):
                    seq_count += 1
        seq_counts.append(seq_count)

    seq_counts.sort()

    return len(output_files), seq_counts


@pytest.fixture(scope="function")
def test_metacoag_spades_run(runner, tmp_dir):
    outpath = tmp_dir
    graph = DATADIR / "5G_metaSPAdes" / "assembly_graph_with_scaffolds.gfa"
    contigs = DATADIR / "5G_metaSPAdes" / "contigs.fasta"
    paths = DATADIR / "5G_metaSPAdes" / "contigs.paths"
    abundance = DATADIR / "5G_metaSPAdes" / "coverm_mean_coverage.tsv"
    args = f"--assembler spades --graph {graph} --contigs {contigs} --paths {paths} --abundance {abundance} --output {outpath}".split()
    r = runner.invoke(metacoag, args, catch_exceptions=False)

    assert r.exit_code == 0, r.output  # Check if the command ran successfully

    n_bins, seq_counts = get_files_and_seq_counts(outpath / "bins")
    return n_bins, seq_counts


@pytest.fixture(scope="function")
def test_metacoag_megahit_run(runner, tmp_dir):
    outpath = tmp_dir
    graph = DATADIR / "5G_MEGAHIT" / "final.gfa"
    contigs = DATADIR / "5G_MEGAHIT" / "final.contigs.fa"
    abundance = DATADIR / "5G_MEGAHIT" / "abundance.tsv"
    args = f"--assembler megahit --graph {graph} --contigs {contigs} --abundance {abundance} --output {outpath}".split()
    r = runner.invoke(metacoag, args, catch_exceptions=False)

    assert r.exit_code == 0, r.output  # Check if the command ran successfully

    n_bins, seq_counts = get_files_and_seq_counts(outpath / "bins")
    return n_bins, seq_counts


@pytest.fixture(scope="function")
def test_metacoag_flye_run(tmp_dir, runner):
    outpath = tmp_dir
    graph = DATADIR / "1Y3B_Flye" / "assembly_graph.gfa"
    contigs = DATADIR / "1Y3B_Flye" / "assembly.fasta"
    paths = DATADIR / "1Y3B_Flye" / "assembly_info.txt"
    abundance = DATADIR / "1Y3B_Flye" / "abundance.tsv"
    args = f"--assembler flye --graph {graph} --contigs {contigs} --paths {paths} --abundance {abundance} --output {outpath}".split()
    r = runner.invoke(metacoag, args, catch_exceptions=False)

    assert r.exit_code == 0, r.output

    n_bins, seq_counts = get_files_and_seq_counts(outpath / "bins")
    return n_bins, seq_counts


def test_n_bins_metacoag_spades(test_metacoag_spades_run):
    n_bins, seq_counts = test_metacoag_spades_run

    # Assert number of bins
    assert n_bins == 5

    # Assert bin sizes
    assert seq_counts == [10, 23, 48, 69, 78]


@pytest.mark.filterwarnings("ignore::RuntimeWarning")
def test_n_bins_metacoag_megahit(test_metacoag_megahit_run):
    n_bins, seq_counts = test_metacoag_megahit_run

    # Assert number of bins
    assert n_bins == 5

    # Assert bin sizes
    assert seq_counts == [36, 40, 46, 84, 127]


@pytest.mark.filterwarnings("ignore::RuntimeWarning")
def test_n_bins_metacoag_flye(test_metacoag_flye_run):
    n_bins, seq_counts = test_metacoag_flye_run

    # Assert number of bins
    assert n_bins == 3

    # Assert bin sizes
    assert seq_counts == [1, 1, 1]
