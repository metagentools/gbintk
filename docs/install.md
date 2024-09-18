# Installing GraphBin-Tk

GraphBin-Tk is now available on [bioconda](https://anaconda.org/bioconda/gbintk) and [PyPI](https://pypi.org/project/gbintk/).

### Using conda

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

# install graphbin
conda install -c bioconda gbintk

# check graphbin installation
gbintk --help
```

### Using pip

You can install GraphBin-Tk using `pip` from the [PyPI](https://pypi.org/project/gbintk/) distribution.

```shell
pip install gbintk
```