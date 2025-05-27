import pathlib
import pytest
import subprocess


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


def exec_command(cmnd, stdout=subprocess.PIPE, stderr=subprocess.PIPE):
    """executes shell command and returns stdout if completes exit code 0

    Parameters
    ----------

    cmnd : str
      shell command to be executed
    stdout, stderr : streams
      Default value (PIPE) intercepts process output, setting to None
      blocks this."""

    proc = subprocess.Popen(cmnd, shell=True, stdout=stdout, stderr=stderr)
    out, err = proc.communicate()
    if proc.returncode != 0:
        raise RuntimeError(f"FAILED: {cmnd}\n{err}")
    return out.decode("utf8") if out is not None else None


def test_gbintk():
    """test gbintk"""
    cmd = "gbintk --help"
    exec_command(cmd)


def test_gbintk_version():
    """test gbintk version"""
    cmd = "gbintk --version"
    exec_command(cmd)


def test_gbintk_graphbin():
    """test gbintk graphbin"""
    cmd = "gbintk graphbin --help"
    exec_command(cmd)


def test_gbintk_graphbin2():
    """test gbintk graphbin2"""
    cmd = "gbintk graphbin2 --help"
    exec_command(cmd)


def test_gbintk_metacoag():
    """test gbintk metacoag"""
    cmd = "gbintk metacoag --help"
    exec_command(cmd)


def test_gbintk_prepare():
    """test gbintk prepare"""
    cmd = "gbintk prepare --help"
    exec_command(cmd)


def test_gbintk_visualise():
    """test gbintk visualise"""
    cmd = "gbintk visualise --help"
    exec_command(cmd)


def test_gbintk_evaluate():
    """test gbintk evaluate"""
    cmd = "gbintk evaluate --help"
    exec_command(cmd)