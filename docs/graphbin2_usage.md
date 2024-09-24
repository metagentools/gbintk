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
  --delimiter [comma|tab]         delimiter for input/output results. Supports
                                  a comma and a tab.  [default: comma]
  --nthreads INTEGER              number of threads to use.  [default: 8]
  -h, --help                      Show this message and exit.
```


## Input Format

The SPAdes version of GraphBin2 takes in 4 files as inputs (required).

* Contigs file (in `.fasta` format)
* Assembly graph file (in `.gfa` format)
* Paths of contigs (in `.paths` format)
* Binning output from an existing tool (in `.csv` format)

The MEGAHIT version of GraphBin2 takes in 4 files as inputs (required).

* Contigs file (in `.fasta` format)
* Abundance file (tab separated file with contig ID and coverage in each line)
* Assembly graph file (in `.gfa` format)
* Binning output from an existing tool (in `.csv` format)

The Flye version of GraphBin2 takes in 4 files as inputs (required).

* Contigs file (in `.fasta` format)
* Abundance file (tab separated file with contig ID and coverage in each line)
* Assembly graph file (in `.gfa` format)
* Binning output from an existing tool (in `.csv` format)

**Note:** Make sure that the initial binning result consists of contigs belonging to only one bin. GraphBin2 is designed to handle initial contigs which belong to only one bin.


## Example Usage

```shell
# SPAdes assembly
gbintk graphbin2 --assembler spades --contigs /path/to/contigs.fasta --paths /path/to/paths_file.paths --graph /path/to/graph_file.gfa  --binned /path/to/binning_result.csv --abundance /path/to/abundance.tsv --output /path/to/output_folder

# MEGAHIT version
gbintk graphbin2 --assembler megahit --graph /path/to/final.gfa --contigs /path/to/final.contigs.fa --binned /path/to/binning_result.csv --abundance /path/to/abundance.tsv --output /path/to/output_folder

# Flye assembly
gbintk graphbin2 --assembler flye --contigs /path/to/assembly.fasta --paths /path/to/assembly_info.txt --graph /path/to/graph_file.gfa --binned /path/to/binning_result.csv --abundance /path/to/abundance.tsv --output /path/to/output_folder
```

## Output

The output of GraphBin2 will contain the following main files and folders.

* `graphbin2_output.csv` file with comma separated values ```(contig_identifier, bin_identifier)``` for the refined binning result.
* `bins` folder containing `.fasta` files of the refined bins. The bins include shared contigs as well.