# Using GraphBin2

Run `gbintk graphbin2 --help` or `gbintk graphbin2 -h` to list the help message for GraphBin2.

```shell
Usage: gbintk graphbin2 [OPTIONS]

  GraphBin2: Refined and Overlapped Binning of Metagenomic Contigs Using
  Assembly Graphs

Options:
  --assembler [spades|megahit|flye]
                                  name of the assembler used (SPAdes, MEGAHIT
                                  or Flye)  [required]
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