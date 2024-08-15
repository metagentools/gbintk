# Formatting binning results for GraphBin/GraphBin2

Run `gbintk prepare --help` or `gbintk prepare -h` to list the help message for formatting.

```shell
Usage: gbintk prepare [OPTIONS]

  Format the initial binning result from an existing binning tool

Options:
  --assembler [spades|megahit|flye]
                                  name of the assembler used (SPAdes, MEGAHIT
                                  or Flye)  [required]
  --resfolder PATH                path to the folder containing FASTA files
                                  for individual bins  [required]
  --delimiter [,|;|     |" "]         delimiter for input/output results. Supports
                                  a comma (,), a semicolon (;), a tab ($'\t'),
                                  a space (" ") and a pipe (|)  [default: ,]
  --prefix TEXT                   prefix for the output file
  --output PATH                   path to the output folder  [required]
  -h, --help                      Show this message and exit.
```