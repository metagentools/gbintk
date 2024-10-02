# GraphBin-Tk: assembly graph-based metagenomic binning toolkit

![GitHub License](https://img.shields.io/github/license/metagentools/gbintk)
[![status](https://joss.theoj.org/papers/4647b0df563fc570f1550e721718ac17/status.svg)](https://joss.theoj.org/papers/4647b0df563fc570f1550e721718ac17)
[![install with bioconda](https://img.shields.io/badge/install%20with-bioconda-brightgreen.svg?style=flat)](http://bioconda.github.io/recipes/gbintk/README.html)
[![Conda](https://img.shields.io/conda/v/bioconda/gbintk)](https://anaconda.org/bioconda/gbintk)
[![PyPI version](https://badge.fury.io/py/gbintk.svg)](https://badge.fury.io/py/gbintk)
[![CI](https://github.com/metagentools/gbintk/actions/workflows/testing_python_app.yml/badge.svg)](https://github.com/metagentools/gbintk/actions/workflows/testing_python_app.yml)
[![codecov](https://codecov.io/gh/metagentools/gbintk/graph/badge.svg?token=r5sniGexZG)](https://codecov.io/gh/metagentools/gbintk)
[![CodeQL](https://github.com/metagentools/gbintk/actions/workflows/codeql.yml/badge.svg)](https://github.com/metagentools/gbintk/actions/workflows/codeql.yml)
[![Documentation Status](https://readthedocs.org/projects/gbintk/badge/?version=latest)](https://gbintk.readthedocs.io/en/latest/?badge=latest)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

GraphBin-Tk combines assembly graph-based metagenomic bin-refinement and binning techniques [GraphBin](https://github.com/metagentools/GraphBin), [GraphBin2](https://github.com/metagentools/GraphBin2) and [MetaCoAG](https://github.com/metagentools/MetaCoAG) along with additional processing functionality to visualise and evaluate results, into one comprehensive toolkit.

<p align="center">
  <img src="https://raw.githubusercontent.com/metagentools/gbintk/master/docs/images/gbintk_workflow.png" width="800" title="Initial binning" alt="Initial binning">
</p>

For detailed instructions on installation and usage, please refer to the documentation hosted at **[Read the Docs](https://gbintk.readthedocs.io/en/latest/)**.

**NEW:** GraphBin-Tk is now available on [bioconda](https://anaconda.org/bioconda/gbintk) and [PyPI](https://pypi.org/project/gbintk/).

## Installing GraphBin-Tk

### Using conda

You can install GraphBin-Tk using the [bioconda](https://anaconda.org/bioconda/gbintk) distribution. You can download `conda` from 
[Anaconda](https://www.anaconda.com/distribution/) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html). You can also use [`mamba`](https://mamba.readthedocs.io/en/latest/index.html) instead of `conda`.

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

### Using pip

You can install GraphBin-Tk using `pip` from the [PyPI](https://pypi.org/project/gbintk/) distribution.

```shell
# install gbintk
pip install gbintk

# check gbintk installation
gbintk --help
```

### For development

Please follow the steps below to install `gbintk` using `flit` for development.

```shell
# clone repository
git clone https://github.com/metagentools/gbintk.git

# move to gbintk directory
cd gbintk

# create and activate conda env
conda env create -f environment.yml
conda activate gbintk

# install using flit
flit install -s --python `which python`

# test installation
gbintk --help
```

## Available subcommands in GraphBin-Tk

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

Please refer to [DEMO.md](https://github.com/metagentools/gbintk/blob/main/DEMO.md) for example code to run using test data provided. For further details on available subcommands and examples, please refer to the documentation hosted at **[Read the Docs](https://gbintk.readthedocs.io/en/latest/)**.

## Citation

If you use GraphBin-Tk in your work, please cite the relevant tools.

**GraphBin**
> Vijini Mallawaarachchi, Anuradha Wickramarachchi, Yu Lin. GraphBin: Refined binning of metagenomic contigs using assembly graphs. Bioinformatics, Volume 36, Issue 11, June 2020, Pages 3307–3313, DOI: [https://doi.org/10.1093/bioinformatics/btaa180](https://doi.org/10.1093/bioinformatics/btaa180)

**GraphBin2**
> Vijini G. Mallawaarachchi, Anuradha S. Wickramarachchi, and Yu Lin. GraphBin2: Refined and Overlapped Binning of Metagenomic Contigs Using Assembly Graphs. In 20th International Workshop on Algorithms in Bioinformatics (WABI 2020). Leibniz International Proceedings in Informatics (LIPIcs), Volume 172, pp. 8:1-8:21, Schloss Dagstuhl – Leibniz-Zentrum für Informatik (2020). DOI: [https://doi.org/10.4230/LIPIcs.WABI.2020.8](https://doi.org/10.4230/LIPIcs.WABI.2020.8)

> Mallawaarachchi, V.G., Wickramarachchi, A.S. & Lin, Y. Improving metagenomic binning results with overlapped bins using assembly graphs. Algorithms Mol Biol 16, 3 (2021). DOI:  [https://doi.org/10.1186/s13015-021-00185-6](https://doi.org/10.1186/s13015-021-00185-6)

**MetaCoAG**
> Mallawaarachchi, V., Lin, Y. (2022). MetaCoAG: Binning Metagenomic Contigs via Composition, Coverage and Assembly Graphs. In: Pe'er, I. (eds) Research in Computational Molecular Biology. RECOMB 2022. Lecture Notes in Computer Science(), vol 13278. Springer, Cham. DOI: [https://doi.org/10.1007/978-3-031-04749-7_5](https://doi.org/10.1007/978-3-031-04749-7_5)

> Vijini Mallawaarachchi and Yu Lin. Accurate Binning of Metagenomic Contigs Using Composition, Coverage, and Assembly Graphs. Journal of Computational Biology 2022 29:12, 1357-1376. DOI: [https://doi.org/10.1089/cmb.2022.0262](https://doi.org/10.1089/cmb.2022.0262)

## Funding

GraphBin-Tk is funded by an [Essential Open Source Software for Science 
Grant](https://chanzuckerberg.com/eoss/proposals/cogent3-python-apis-for-iq-tree-and-graphbin-via-a-plug-in-architecture/) 
from the Chan Zuckerberg Initiative.

<p align="left">
  <img src="https://chanzuckerberg.com/wp-content/themes/czi/img/logo.svg" width="300">
</p>
