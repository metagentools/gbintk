# Using MetaCoAG

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
  --delimiter [,|;|$'\t'|" "]     delimiter for input/output results. Supports
                                  a comma (,), a semicolon (;), a tab ($'\t'),
                                  a space (" ") and a pipe (|)  [default: ,]
  --nthreads INTEGER              number of threads to use.  [default: 8]
  -h, --help                      Show this message and exit.
```