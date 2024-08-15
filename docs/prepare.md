# Formatting binning results for GraphBin/GraphBin2

You can use the `prepare` subcommand of `gbintk` to format the binning results so they are accepted by GraphBin/GraphBin2.

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

## Example usage

You can use the `prepare` subcommand to format an initial binning result in to the `.csv` format (by default) with contig identifiers and bin ID. Contigs are named according to their original identifier and bins are numbered according to the fasta file name. You can run the `prepare` subcommand as follows.

```shell
# For SPAdes
gbintk prepare --assembler spades ----resfolder /path/to/folder_with_binning_result --output /path/to/output_folder

# For MEGAHIT
gbintk prepare --assembler megahit ----resfolder /path/to/folder_with_binning_result --output /path/to/output_folder

# For Flye
gbintk prepare --assembler flye ----resfolder /path/to/folder_with_binning_result --output /path/to/output_folder
```

## Output

Formatted binning result will be stored in a file named `initial_contig_bins.csv` in the output folder provided. This file would look as below.

```
contig-1,bin-1
contig-2,bin-1
contig-3,bin-2
contig-4,bin-2
contig-5,bin-3
...
```