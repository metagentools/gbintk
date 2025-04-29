# Using GraphBin2

A formatted initial binning result from the `prepare` subcommand can be improved by providing it to GraphBin2 using the subcommand `graphbin2`.

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
  --delimiter [comma|tab]         delimiter for input/output results. Supports
                                  a comma and a tab.  [default: comma]
  --nthreads INTEGER              number of threads to use.  [default: 8]
  -h, --help                      Show this message and exit.
```


## Input Format

The SPAdes version of GraphBin2 takes in 5 files as inputs (required).

* Contigs file (in `.fasta` format)
* Assembly graph file (in `.gfa` format)
* Contig paths file (in `.paths` format)
* A delimited text file containing the initial binning result (e.g.`<contig_id>,<groud_truth_bin>` in `.csv` format)
* A tab delimited file containing the contig identifier and its average read coverage for each contig - A `.tsv` can be obtained by running a read coverage calculation tool such as [CoverM](https://github.com/wwood/CoverM) or [Koverage](https://github.com/beardymcjohnface/Koverage).

The MEGAHIT version of GraphBin2 takes in 4 files as inputs (required).

* Contigs file (in `.fasta` format)
* Assembly graph file (in `.gfa` format)
* A delimited text file containing the initial binning result (e.g.`<contig_id>,<groud_truth_bin>` in `.csv` format)
* A tab delimited file containing the contig identifier and its average read coverage for each contig

The Flye version of GraphBin2 takes in 5 files as inputs (required).

* Assembly graph file (`assembly_graph.gfa`)
* Contigs file (`assembly.fasta`)
* Contig paths file (`assembly_info.txt`)
* A delimited text file containing the initial binning result (e.g.`<contig_id>,<groud_truth_bin>` in `.csv` format)
* A tab delimited file containing the contig identifier and its average read coverage for each contig

**Note:** Make sure that the initial binning result consists of contigs belonging to only one bin. GraphBin2 is designed to handle initial contigs which belong to only one bin.


## Example Usage

```shell
# SPAdes assembly available in tests/data/
gbintk graphbin2 --assembler spades --graph tests/data/5G_metaSPAdes/assembly_graph_with_scaffolds.gfa  --contigs tests/data/5G_metaSPAdes/contigs.fasta --paths tests/data/5G_metaSPAdes/contigs.paths --binned tests/data/5G_metaSPAdes/initial_contig_bins.csv --abundance tests/data/5G_metaSPAdes/abundance.tsv --output tests/data/5G_metaSPAdes/graphbin2_results

# MEGAHIT assembly available in tests/data/
gbintk graphbin2 --assembler megahit --graph tests/data/5G_MEGAHIT/final.gfa --contigs tests/data/5G_MEGAHIT/final.contigs.fa --binned tests/data/5G_MEGAHIT/initial_contig_bins.csv --abundance tests/data/5G_MEGAHIT/abundance.tsv --output tests/data/5G_MEGAHIT/graphbin2_results

# Flye assembly available in tests/data/
gbintk graphbin2 --assembler flye --contigs tests/data/1Y3B_Flye/assembly.fasta --paths tests/data/1Y3B_Flye/assembly_info.txt --graph tests/data/1Y3B_Flye/graph_file.gfa --binned tests/data/1Y3B_Flye/initial_contig_bins.csv --abundance tests/data/1Y3B_Flye/abundance.tsv --output tests/data/1Y3B_Flye/graphbin2_results
```

## Output

The output of GraphBin2 will contain the following main files and folders.

* A delimited text file containing the contig identifier and bin identifier for each binned contig (e.g. `graphbin2_output.csv`).
* `bins` folder containing `.fasta` files of the refined bins. The bins include shared contigs as well.
* Shared contigs and their corresponding bins can be found in the `graphbin2.log` file.