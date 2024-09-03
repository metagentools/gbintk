import pathlib
import pytest

from click.testing import CliRunner

from gbintk.cli import visualise
from PIL import Image, UnidentifiedImageError

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
def out_file_names():
    """output file names without file type."""
    return ["final_GraphBin_binning_result", "initial_binning_result"]


@pytest.fixture(scope="session")
def runner():
    """exportrc works correctly."""
    return CliRunner()


def test_visualise_spades_run(runner, tmp_dir, out_file_names):
    outpath = tmp_dir
    initial = DATADIR / "5G_metaSPAdes" / "metacoag_res.csv"
    final = DATADIR / "5G_metaSPAdes" / "graphbin_res.csv"
    graph = DATADIR / "5G_metaSPAdes" / "assembly_graph_with_scaffolds.gfa"
    contigs = DATADIR / "5G_metaSPAdes" / "contigs.fasta"
    paths = DATADIR / "5G_metaSPAdes" / "contigs.paths"
    args = f"--assembler spades --initial {initial} --final {final} --graph {graph} --contigs {contigs} --paths {paths} --output {outpath}".split()
    r = runner.invoke(visualise, args, catch_exceptions=False)

    assert r.exit_code == 0, r.output

    for out_file in out_file_names:
        image_file = outpath / (out_file + ".png")
        with Image.open(image_file) as im:
            im.verify()  # Raises an exception if the file is malformatted
            assert im.format == "PNG"
            assert im.size == (2000, 2000)
            assert im.mode == "RGB"


def test_visualise_megahit_run(runner, tmp_dir, out_file_names):
    outpath = tmp_dir
    initial = DATADIR / "5G_MEGAHIT" / "initial_contig_bins.csv"
    final = DATADIR / "5G_MEGAHIT" / "graphbin_output.csv"
    graph = DATADIR / "5G_MEGAHIT" / "final.gfa"
    contigs = DATADIR / "5G_MEGAHIT" / "final.contigs.fa"
    args = f"--assembler megahit --initial {initial} --final {final} --graph {graph} --contigs {contigs} --output {outpath}".split()
    r = runner.invoke(visualise, args, catch_exceptions=False)

    assert r.exit_code == 0, r.output

    for out_file in out_file_names:
        image_file = outpath / (out_file + ".png")
        with Image.open(image_file) as im:
            im.verify()  # Raises an exception if the file is malformatted
            assert im.format == "PNG"
            assert im.size == (2000, 2000)
            assert im.mode == "RGB"


def test_visualise_flye_run(runner, tmp_dir, out_file_names):
    outpath = tmp_dir
    initial = DATADIR / "1Y3B_Flye" / "initial_contig_bins.csv"
    final = DATADIR / "1Y3B_Flye" / "graphbin_output.csv"
    graph = DATADIR / "1Y3B_Flye" / "assembly_graph.gfa"
    contigs = DATADIR / "1Y3B_Flye" / "assembly.fasta"
    paths = DATADIR / "1Y3B_Flye" / "assembly_info.txt"
    args = f"--assembler flye --initial {initial} --final {final} --graph {graph} --contigs {contigs} --paths {paths} --output {outpath}".split()
    r = runner.invoke(visualise, args, catch_exceptions=False)

    assert r.exit_code == 0, r.output

    for out_file in out_file_names:
        image_file = outpath / (out_file + ".png")
        with Image.open(image_file) as im:
            im.verify()  # Raises an exception if the file is malformatted
            assert im.format == "PNG"
            assert im.size == (2000, 2000)
            assert im.mode == "RGB"


@pytest.mark.parametrize("prefix", ["test", "test_", "test__"])
def test_visualise_prefix(runner, tmp_dir, out_file_names, prefix):
    outpath = tmp_dir
    initial = DATADIR / "5G_metaSPAdes" / "metacoag_res.csv"
    final = DATADIR / "5G_metaSPAdes" / "graphbin_res.csv"
    graph = DATADIR / "5G_metaSPAdes" / "assembly_graph_with_scaffolds.gfa"
    contigs = DATADIR / "5G_metaSPAdes" / "contigs.fasta"
    paths = DATADIR / "5G_metaSPAdes" / "contigs.paths"
    args = f"--assembler spades --initial {initial} --final {final} --graph {graph} --contigs {contigs} --paths {paths} --prefix {prefix} --output {outpath}".split()
    r = runner.invoke(visualise, args, catch_exceptions=False)

    assert r.exit_code == 0, r.output

    expected_prefix = prefix if prefix.endswith("_") else prefix + "_"

    for out_file in out_file_names:
        image_file = outpath / (expected_prefix + out_file + ".png")
        with Image.open(image_file) as im:
            im.verify()  # Raises an exception if the file is malformatted
            assert im.format == "PNG"
            assert im.size == (2000, 2000)
            assert im.mode == "RGB"


@pytest.mark.parametrize(
    "img_type",
    ["png", "eps", "pdf", "svg"],
)
def test_visualise_imgtype(runner, tmp_dir, out_file_names, img_type):
    outpath = tmp_dir
    initial = DATADIR / "5G_metaSPAdes" / "metacoag_res.csv"
    final = DATADIR / "5G_metaSPAdes" / "graphbin_res.csv"
    graph = DATADIR / "5G_metaSPAdes" / "assembly_graph_with_scaffolds.gfa"
    contigs = DATADIR / "5G_metaSPAdes" / "contigs.fasta"
    paths = DATADIR / "5G_metaSPAdes" / "contigs.paths"
    args = f"--assembler spades --initial {initial} --final {final} --graph {graph} --contigs {contigs} --paths {paths} --imgtype {img_type} --output {outpath}".split()
    r = runner.invoke(visualise, args, catch_exceptions=False)

    assert r.exit_code == 0, r.output

    for out_file in out_file_names:
        image_file = outpath / (out_file + f".{img_type}")
        try:
            with Image.open(image_file) as im:
                im.verify()  # Raises an exception if the file is malformatted
                assert im.format == img_type.upper()
                assert im.size == (2000, 2000)
                assert im.mode == "RGB"
        except UnidentifiedImageError:  # pillow doesn't support pdf/svg
            with open(image_file, "rb") as f:
                assert len(f.read())


def test_visualise_outdir(runner, tmp_dir, out_file_names):
    outpath = tmp_dir / "testing"
    initial = DATADIR / "5G_metaSPAdes" / "metacoag_res.csv"
    final = DATADIR / "5G_metaSPAdes" / "graphbin_res.csv"
    graph = DATADIR / "5G_metaSPAdes" / "assembly_graph_with_scaffolds.gfa"
    contigs = DATADIR / "5G_metaSPAdes" / "contigs.fasta"
    paths = DATADIR / "5G_metaSPAdes" / "contigs.paths"
    args = f"--assembler spades --initial {initial} --final {final} --graph {graph} --contigs {contigs} --paths {paths} --output {outpath}".split()
    r = runner.invoke(visualise, args, catch_exceptions=False)

    assert r.exit_code == 0, r.output

    for out_file in out_file_names:
        image_file = outpath / (out_file + ".png")
        with Image.open(image_file) as im:
            im.verify()  # Raises an exception if the file is malformatted
            assert im.format == "PNG"
            assert im.size == (2000, 2000)
            assert im.mode == "RGB"
