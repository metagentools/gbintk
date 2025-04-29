# Using GraphBin

A formatted initial binning result from the `prepare` subcommand can be improved by providing it to GraphBin using the subcommand `graphbin`.

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
  --delimiter [comma|tab]         delimiter for input/output results. Supports
                                  a comma and a tab.  [default: comma]
  -h, --help                      Show this message and exit.
```

`max_iteration` and `diff_threshold` parameters are set by default to `100` and `0.1` respectively. However, the user can specify them when running GraphBin.

## Input Format

For the SPAdes version, GraphBin takes in 4 files as inputs (required).

* Assembly graph file (in `.gfa` format)
* Contigs file (in `.fasta` format)
* Contig paths file (`.paths` format)
* A delimited text file containing the initial binning result (e.g.`<contig_id>,<groud_truth_bin>` in `.csv` format)

For the MEGAHIT version, GraphBin takes in 3 files as inputs (required).

* Assembly graph file (in `.gfa` format)
* Contigs file (in `.fasta` format)
* A delimited text file containing the initial binning result (e.g.`<contig_id>,<groud_truth_bin>` in `.csv` format)

For the Flye version, GraphBin takes in 4 files as inputs (required).

* Assembly graph file (`assembly_graph.gfa`)
* Contigs file (`assembly.fasta`)
* Contig paths file (`assembly_info.txt`)
* A delimited text file containing the initial binning result (e.g.`<contig_id>,<groud_truth_bin>` in `.csv` format)

**Note:** Make sure that the initial binning result consists of contigs belonging to only one bin. GraphBin is designed to handle initial contigs which belong to only one bin. Multiple bins for the initial contigs are not supported.

**Note:** You can specify the delimiter for the initial binning result file and the final output file using the delimiter paramter. Supports comma (`comma`) and tab (`tab`).

## Example Usage

```shell
# SPAdes assembly available in tests/data/
gbintk graphbin --assembler spades --graph tests/data/5G_metaSPAdes/assembly_graph_with_scaffolds.gfa --contigs tests/data/5G_metaSPAdes/contigs.fasta --paths tests/data/5G_metaSPAdes/contigs.paths --binned tests/data/5G_metaSPAdes/initial_contig_bins.csv --output tests/data/5G_metaSPAdes/graphbin_results

# MEGAHIT assembly available in tests/data/
gbintk graphbin --assembler megahit --graph tests/data/5G_MEGAHIT/final.gfa --contigs tests/data/5G_MEGAHIT/final.contigs.fa --binned tests/data/5G_MEGAHIT/initial_contig_bins.csv --output tests/data/5G_MEGAHIT/graphbin_results

# Flye assembly available in tests/data/
gbintk graphbin --assembler flye --graph tests/data/1Y3B_Flye/assembly_graph.gfa --contigs tests/data/1Y3B_Flye/assembly.fasta --paths tests/data/1Y3B_Flye/assembly_info.txt --binned tests/data/1Y3B_Flye/initial_contig_bins.csv --output tests/data/1Y3B_Flye/graphbin_results
```

## Output

The output of GraphBin will contain the following main files and folders.

* A delimited text file containing the contig identifier and bin identifier for each binned contig (e.g. `graphbin_output.csv`).
* A delimited text file containing the contig identifier and bin identifier for each unbinned contig (e.g. `graphbin_unbinned.csv`).
* `bins` folder containing `.fasta` files of the refined bins.