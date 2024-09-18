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