# Installing GraphBin-Tk

GraphBin-Tk is now available on [bioconda](https://anaconda.org/bioconda/gbintk) and [PyPI](https://pypi.org/project/gbintk/).

## Using conda

You can install GraphBin-Tk using the [bioconda](https://anaconda.org/bioconda/gbintk) distribution. You can download 
[Anaconda](https://www.anaconda.com/distribution/) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) which contains `conda`. You can also use [`mamba`](https://mamba.readthedocs.io/en/latest/index.html) instead of `conda`.

```shell
# add channels
conda config --add channels defaults
conda config --add channels bioconda
conda config --add channels conda-forge

# create conda environment
conda create -n gbintk

# activate conda environment
conda activate gbintk

# install gbintk
conda install -c bioconda gbintk

# check gbintk installation
gbintk --help
```

## Using pip

You can install GraphBin-Tk using `pip` from the [PyPI](https://pypi.org/project/gbintk/) distribution.

```shell
# install gbintk
pip install gbintk

# check gbintk installation
gbintk --help
```

## Dependencies and external software checklist

Please make sure that the following dependencies and external software are properly installed before running GraphBin-Tk.

* [`python>=3.9,<3.13`](https://www.python.org/)
* [`cogent3`](https://cogent3.org/)
* [`igraph`](https://python.igraph.org/en/stable/)
* [`cairocffi`](https://pypi.org/project/cairocffi/)
* [`pycairo`](https://pypi.org/project/pycairo/)
* [`networkx`](https://networkx.org/)
* [`scipy`](https://scipy.org/)
* [`numpy`](https://numpy.org/)
* [`pandas`](https://pandas.pydata.org/)
* [`tqdm`](https://tqdm.github.io/)
* [`click`](https://click.palletsprojects.com/en/stable/)
* [`tabulate`](https://pypi.org/project/tabulate/)
* [`graphbin`](https://graphbin.readthedocs.io/en/latest/)
* [`graphbin2>=1.3.3`](https://graphbin2.readthedocs.io/en/latest/)
* [`metacoag>=1.2.1`](https://metacoag.readthedocs.io/en/stable/)
* [`fraggenescan`](https://sourceforge.net/projects/fraggenescan/)
* [`hmmer`](http://hmmer.org/)

You will need one of the following assemblers to obtain the metagenome assemblies depending on your read data.

* [spades](https://github.com/ablab/spades)
* [megahit](https://github.com/voutcn/megahit)
* [flye](https://github.com/mikolmogorov/Flye)

## Available subcommands

Run `gbintk --help` or `gbintk -h` to list the help message for GraphBin-Tk.

```shell
Usage: gbintk [OPTIONS] COMMAND [ARGS]...

  gbintk (GraphBin-Tk): Assembly graph-based metagenomic binning toolkit

Options:
  -v, --version  Show the version and exit.
  -h, --help     Show this message and exit.

Commands:
  graphbin   GraphBin: Refined Binning of Metagenomic Contigs using...
  graphbin2  GraphBin2: Refined and Overlapped Binning of Metagenomic...
  metacoag   MetaCoAG: Binning Metagenomic Contigs via Composition,...
  prepare    Format the initial binning result from an existing binning tool
  visualise  Visualise binning and refinement results
  evaluate   Evaluate the binning results given a ground truth
```