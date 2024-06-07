# GraphBin-Tk: Assembly graph-based metagenomic binning toolkit

![GitHub License](https://img.shields.io/github/license/metagentools/gbintk)
[![CI](https://github.com/metagentools/gbintk/actions/workflows/testing_python_app.yml/badge.svg)](https://github.com/metagentools/gbintk/actions/workflows/testing_python_app.yml)
[![codecov](https://codecov.io/gh/metagentools/gbintk/graph/badge.svg?token=r5sniGexZG)](https://codecov.io/gh/metagentools/gbintk)
[![CodeQL](https://github.com/metagentools/gbintk/actions/workflows/codeql.yml/badge.svg)](https://github.com/metagentools/gbintk/actions/workflows/codeql.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

GraphBin-Tk combines assembly graph-based metagenomic bin-refinement and binning techniques [GraphBin](https://github.com/metagentools/GraphBin), [GraphBin2](https://github.com/metagentools/GraphBin2) and [MetaCoAG](https://github.com/metagentools/MetaCoAG) into one comprehensive toolkit.

## Available commands

Run `gbintk --help` or `gbintk -h` to list the help message for GraphBin-Tk.

```bash
Usage: gbintk [OPTIONS] COMMAND [ARGS]...

  gbintk (GraphBin-Tk): Assembly graph-based metagenomic binning toolkit

Options:
  -v, --version  Show the version and exit.
  -h, --help     Show this message and exit.

Commands:
  graphbin   GraphBin: Refined Binning of Metagenomic Contigs using...
  graphbin2  GraphBin2: Refined and Overlapped Binning of Metagenomic...
  metacoag   MetaCoAG: Binning Metagenomic Contigs via Composition,...
```

### `gbintk graphbin`: Run [GraphBin](https://github.com/metagentools/GraphBin)

Run `gbintk graphbin --help` or `gbintk graphbin -h` to list the help message for GraphBin.

```bash
Usage: gbintk graphbin [OPTIONS]

  GraphBin: Refined Binning of Metagenomic Contigs using Assembly Graphs

Options:
  --assembler [spades|sga|megahit|flye]
                                  name of the assembler used (SPAdes, SGA,
                                  MEGAHIT or Flye)  [required]
  --graph PATH                    path to the assembly graph file  [required]
  --contigs PATH                  path to the contigs file  [required]
  --paths PATH                    path to the contigs.paths (metaSPAdes) or
                                  assembly.info (metaFlye) file
  --binned PATH                   path to the .csv file with the initial
                                  binning output from an existing tool
                                  [required]
  --output PATH                   path to the output folder  [required]
  --prefix TEXT                   prefix for the output file
  --max_iteration INTEGER         maximum number of iterations for label
                                  propagation algorithm  [default: 100]
  --diff_threshold FLOAT RANGE    difference threshold for label propagation
                                  algorithm  [default: 0.1; 0<=x<=1]
  --delimiter [,|;|$'\t'|" "]     delimiter for input/output results. Supports
                                  a comma (,), a semicolon (;), a tab ($'\t'),
                                  a space (" ") and a pipe (|)  [default: ,]
  -h, --help                      Show this message and exit.
```

### `gbintk graphbin2`: Run [GraphBin2](https://github.com/metagentools/GraphBin2)

**NOTE: GraphBin2 feature is still inder constraction. Stay tuned!**

Run `gbintk graphbin2 --help` or `gbintk graphbin2 -h` to list the help message for GraphBin2.

```bash
Usage: gbintk graphbin2 [OPTIONS]

  GraphBin2: Refined and Overlapped Binning of Metagenomic Contigs Using
  Assembly Graphs

Options:
  --assembler [spades|sga|megahit|flye]
                                  name of the assembler used (SPAdes, SGA,
                                  MEGAHIT or Flye)  [required]
  --graph PATH                    path to the assembly graph file  [required]
  --contigs PATH                  path to the contigs file  [required]
  --paths PATH                    path to the contigs.paths (metaSPAdes) or
                                  assembly.info (metaFlye) file
  --abundance PATH                path to the abundance file  [required]
  --binned PATH                   path to the .csv file with the initial
                                  binning output from an existing tool
                                  [required]
  --output PATH                   path to the output folder  [required]
  --prefix TEXT                   prefix for the output file
  --depthb INTEGER                maximum depth for the breadth-first-search.
                                  [default: 5]
  --threshold FLOAT               threshold for determining inconsistent
                                  vertices.  [default: 1.5]
  --delimiter [,|;|$'\t'|" "]     delimiter for input/output results. Supports
                                  a comma (,), a semicolon (;), a tab ($'\t'),
                                  a space (" ") and a pipe (|)  [default: ,]
  --nthreads INTEGER              number of threads to use.  [default: 8]
  -h, --help                      Show this message and exit.
```

### `gbintk metacoag`: Run [MetaCoAG](https://github.com/metagentools/MetaCoAG)

Run `gbintk metacoag --help` or `gbintk metacoag -h` to list the help message for MetaCoAG.

```bash
Usage: gbintk metacoag [OPTIONS]

  MetaCoAG: Binning Metagenomic Contigs via Composition, Coverage and Assembly
  Graphs

Options:
  --assembler [spades|sga|megahit|flye]
                                  name of the assembler used (SPAdes, SGA,
                                  MEGAHIT or Flye)  [required]
  --graph PATH                    path to the assembly graph file  [required]
  --contigs PATH                  path to the contigs file  [required]
  --paths PATH                    path to the contigs.paths (metaSPAdes) or
                                  assembly.info (metaFlye) file
  --abundance PATH                path to the abundance file  [required]
  --output PATH                   path to the output folder  [required]
  --hmm TEXT                      path to marker.hmm file.  [default:
                                  auxiliary/marker.hmm]
  --prefix TEXT                   prefix for the output file
  --min_length INTEGER            minimum length of contigs to consider for
                                  binning.  [default: 1000]
  --p_intra FLOAT RANGE           minimum probability of an edge matching to
                                  assign to the same bin.  [default: 0.1;
                                  0<=x<=1]
  --p_inter FLOAT RANGE           maximum probability of an edge matching to
                                  create a new bin.  [default: 0.01; 0<=x<=1]
  --d_limit INTEGER               distance limit for contig matching.
                                  [default: 20]
  --depthlp INTEGER               depth to consider for label propagation.
                                  [default: 10]
  --n_mg INTEGER                  total number of marker genes.  [default:
                                  108]
  --no_cut_tc                     do not use --cut_tc for hmmsearch.
  --mg_threshold FLOAT RANGE      length threshold to consider marker genes.
                                  [default: 0.5; 0<=x<=1]
  --bin_mg_threshold FLOAT RANGE  minimum fraction of marker genes that should
                                  be present in a bin.  [default: 0.33333;
                                  0<=x<=1]
  --min_bin_size INTEGER          minimum size of a bin to output in base
                                  pairs (bp).  [default: 200000]
  --delimiter [,|;|$'\t'|" "]     delimiter for input/output results. Supports
                                  a comma (,), a semicolon (;), a tab ($'\t'),
                                  a space (" ") and a pipe (|)  [default: ,]
  --nthreads INTEGER              number of threads to use.  [default: 8]
  -h, --help                      Show this message and exit.
```

## Funding

GraphBin-Tk is funded by an [Essential Open Source Software for Science 
Grant](https://chanzuckerberg.com/eoss/proposals/cogent3-python-apis-for-iq-tree-and-graphbin-via-a-plug-in-architecture/) 
from the Chan Zuckerberg Initiative.

<p align="left">
  <img src="https://chanzuckerberg.com/wp-content/themes/czi/img/logo.svg" width="300">
</p>
