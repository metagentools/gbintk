import pathlib
import pytest

from click.testing import CliRunner

from gbintk.cli import prepare


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


def test_prepare_spades_res(runner, tmp_dir):
    outpath = tmp_dir
    resfolder = DATADIR / "5G_metaSPAdes" / "initial_bins"
    args = f"--assembler spades --resfolder {resfolder} --output {outpath}".split()
    r = runner.invoke(prepare, args, catch_exceptions=False)
    assert r.exit_code == 0, r.output


def test_prepare_megahit_res(runner, tmp_dir):
    outpath = tmp_dir
    resfolder = DATADIR / "5G_MEGAHIT" / "initial_bins"
    args = f"--assembler megahit --resfolder {resfolder} --output {outpath}".split()
    r = runner.invoke(prepare, args, catch_exceptions=False)
    assert r.exit_code == 0, r.output

