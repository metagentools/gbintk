# Using MetaCoAG

A user can start an analysis by running the `metacoag` subcommand to bin a metagenomic dataset using the metagenomic binning tool MetaCoAG and obtain contig bins or metagenome-assembled genomes (MAGs).

Run `gbintk metacoag --help` or `gbintk metacoag -h` to list the help message for MetaCoAG.

```shell
Usage: gbintk metacoag [OPTIONS]

  MetaCoAG: Binning Metagenomic Contigs via Composition, Coverage and Assembly
  Graphs

Options:
  --assembler [spades|megahit|flye]
                                  name of the assembler used (SPAdes, MEGAHIT
                                  or Flye)  [required]
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
  --delimiter [comma|tab]         delimiter for input/output results. Supports
                                  a comma and a tab.  [default: comma]
  --nthreads INTEGER              number of threads to use.  [default: 8]
  -h, --help                      Show this message and exit.
```

`min_length`, `p_intra`, `p_inter`, `d_limit`, `mg_threshold`, `bin_mg_threshold`, `min_bin_size`, `depthlp` and `nthreads` parameters are set by default to `1000`, `0.1`, `0.01`, `20`, `0.5`, `0.3333`, `200000`, `10` and `8` respectively. However, the user can specify them when running MetaCoAG.

## Input Format

For the *metaSPAdes* version, MetaCoAG takes in 4 files as inputs.

* Assembly graph file (in `.gfa` format)
* Contigs file (in `.fasta` format)
* Contig paths file (in `.paths` format)
* A tab delimited file containing the contig identifier and its average read coverage for each contig. A `.tsv` can be obtained by running a read coverage calculation tool such as [CoverM](https://github.com/wwood/CoverM) or [Koverage](https://github.com/beardymcjohnface/Koverage).

For the *MEGAHIT* version, MetaCoAG takes in 3 files as inputs.

* Assembly graph file (in `.gfa` format)
* Contigs file (in `.fasta` format)
* A tab delimited file containing the contig identifier and its average read coverage for each contig

For the *Flye* version, MetaCoAG takes in 4 files as inputs.

* Assembly graph file (`assembly_graph.gfa`)
* Contigs file (`assembly.fasta`)
* Contig paths file (`assembly_info.txt`)
* A tab delimited file containing the contig identifier and its average read coverage for each contig

**Note:** You can specify the delimiter for the initial binning result file and the final output file using the delimiter paramter. Supports comma (`comma`) and tab (`tab`).

## Example Usage

```shell
# SPAdes assembly available in tests/data/
gbintk metacoag --assembler spades --graph tests/data/5G_metaSPAdes/assembly_graph_with_scaffolds.gfa --contigs tests/data/5G_metaSPAdes/contigs.fasta --paths tests/data/5G_metaSPAdes/contigs.paths --abundance tests/data/5G_metaSPAdes/abundance.tsv --output tests/data/5G_metaSPAdes/metacoag_results

# MEGAHIT assembly available in tests/data/
gbintk metacoag --assembler megahit --graph tests/data/5G_MEGAHIT/final.gfa --contigs tests/data/5G_MEGAHIT/final.contigs.fasta --abundance tests/data/5G_MEGAHIT/abundance.tsv --output tests/data/5G_MEGAHIT/metacoag_results

# Flye assembly available in tests/data/
gbintk metacoag --assembler flye --graph tests/data/1Y3B_Flye/assembly_graph.gfa --contigs tests/data/1Y3B_Flye/assembly.fasta --paths tests/data/1Y3B_Flye/assembly_info.txt --abundance tests/data/1Y3B_Flye/abundance.tsv --output tests/data/1Y3B_Flye/metacoag_results
```

## Output

The output of MetaCoAG will contain the following main files and folders.

* A delimited text file containing the contig identifier and bin identifier for each binned contig (e.g. `contig_to_bin.csv`)
* `bins` containing the identified bins (FASTA file for each bin)
* `low_quality_bins` containing the identified low-quality bins, i.e., having a fraction of marker genes lower than `bin_mg_threshold` (FASTA file for each bin)
* `*.frag.faa`, `*.frag.ffn` and `*.frag.gff` files containing FragGeneScan output
* `*.hmmout` file containing HMMER output