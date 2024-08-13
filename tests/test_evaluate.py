import pathlib
import pytest

from click.testing import CliRunner

from gbintk.cli import evaluate


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


def test_evaluate_run(runner, tmp_dir):
    outpath = tmp_dir
    binned = DATADIR / "5G_metaSPAdes" / "graphbin_res.csv"
    groundtruth = DATADIR / "5G_metaSPAdes" / "ground_truth.csv"
    args = f"--binned {binned} --groundtruth {groundtruth} --output {outpath}".split()
    r = runner.invoke(evaluate, args, catch_exceptions=False)
    assert r.exit_code == 0, r.output
