# Using GraphBin

Run `gbintk graphbin --help` or `gbintk graphbin -h` to list the help message for GraphBin.

```shell
Usage: gbintk graphbin [OPTIONS]

  GraphBin: Refined Binning of Metagenomic Contigs using Assembly Graphs

Options:
  --assembler [spades|megahit|flye]
                                  name of the assembler used (SPAdes, MEGAHIT
                                  or Flye)  [required]
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