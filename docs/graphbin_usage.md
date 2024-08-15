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

`max_iteration` and `diff_threshold` parameters are set by default to `100` and `0.1` respectively. However, the user can specify them when running GraphBin.

## Inputs

For the SPAdes version, GraphBin takes in 3 files as inputs (required).

* Assembly graph file (in `.gfa` format)
* Contigs file (`contigs.fasta` file in FASTA format)
* Paths of contigs (`contigs.paths` file)
* Binning output from an existing tool (in `.csv` format)

For the MEGAHIT version, GraphBin takes in 3 files as inputs (required).

* Assembly graph file (in `.gfa` format. To convert fastg to gfa refer [here](https://github.com/Vini2/GraphBin/blob/master/support/README.md#fastg2gfa))
* Contigs file (in FASTA format)
* Binning output from an existing tool (in `.csv` format)

For the Flye version, GraphBin takes in 3 files as inputs (required).

* Assembly graph file (in `.gfa` format)
* Contigs file (`assembly.fasta` file in FASTA format)
* Paths of contigs (`assembly_info.txt` file)
* Binning output from an existing tool (in `.csv` format)

**Note:** Make sure that the initial binning result consists of contigs belonging to only one bin. GraphBin is designed to handle initial contigs which belong to only one bin. Multiple bins for the initial contigs are not supported.

**Note:** You can specify the delimiter for the initial binning result file and the final output file using the delimiter paramter. Enter the following values for different delimiters; `,` for a comma, `;` for a semicolon, `$'\t'` for a tab, `" "` for a space and `|` for a pipe.

## Example Usage

```shell
# SPAdes assembly
gbintk graphbin --assembler spades --graph /path/to/graph_file.gfa --contigs /path/to/contigs.fasta --paths /path/to/paths_file.paths --binned /path/to/binning_result.csv --output /path/to/output_folder

# MEGAHIT assembly
gbintk graphbin --assembler megahit --graph /path/to/graph_file.gfa --contigs /path/to/contigs.fa --binned /path/to/binning_result.csv --output /path/to/output_folder

# Flye assembly
gbintk graphbin --assembler flye --graph /path/to/assembly_graph.gfa --contigs /path/to/assembly.fasta --paths /path/to/assembly_info.txt --binned /path/to/binning_result.csv --output /path/to/output_folder
```

## Output

The output of GraphBin will contain the following main files and folders.

* `graphbin_output.csv` file with comma separated values ```(contig_identifier, bin_identifier)``` for the refined binning result.
* `graphbin_unbinned.csv` file with names of contigs that were not binned.
* `bins` folder containing `.fasta` files of the refined bins.