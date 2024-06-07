# GraphBin-Tk Demo

## Setup GraphBin-Tk

First, let's download GraphBin-Tk. Make sure you have `git` installed.

```bash
git clone https://github.com/metagentools/gbintk.git
```

Now move in to the 'gbintk' directory.

```bash
cd gbintk
```

Let's create an environment for gbintk using the provided `environment.yml` file. Make sure you have `conda`` installed.

```bash
conda env create -f environment.yml
```

Activate the environment.

```bash
conda activate gbintk
```

Test your installation.

```bash
gbintk --help
```

Now we are all set for the demo.

## Test data

Test data for the demo can be found in the [`tests/data/Sim-5G+metaSPAdes/`](https://github.com/metagentools/gbintk/tree/main/tests/data/Sim-5G%2BmetaSPAdes) folder. Let's set the testing directory path to a variable as shown below so we don't have to type the path every time.

```bash
TESTDIR=tests/data/Sim-5G+metaSPAdes/
```

## Run MetaCoAG

Run the following command to bin the test dataset using MetaCoAG.

```bash
gbintk metacoag --assembler spades --graph $TESTDIR/assembly_graph_with_scaffolds.gfa --contigs $TESTDIR/contigs.fasta --paths $TESTDIR/contigs.paths --abundance $TESTDIR/coverm_mean_coverage.tsv --output $TESTDIR
```

## Run GraphBin

Run the following command to refine the binning results using GraphBin.

```bash
gbintk graphbin --assembler spades --graph $TESTDIR/assembly_graph_with_scaffolds.gfa --contigs $TESTDIR/contigs.fasta --paths $TESTDIR/contigs.paths --binned $TESTDIR/contig_to_bin.tsv --output $TESTDIR
```

## Visualise binning results

Run the following command to visualise the original binning result and the refined binning results on the assembly graph.

```bash
gbintk visualise --assembler spades --initial $TESTDIR/contig_to_bin.tsv --final $TESTDIR/graphbin_output.csv --graph $TESTDIR/assembly_graph_with_scaffolds.gfa --paths $TESTDIR/contigs.paths --output $TESTDIR --width 2500 --height 2500
```

Below are some example visualisations generated.

**Initial binning result**

<p align="center">
  <img src="https://raw.githubusercontent.com/metagentools/gbintk/master/docs/initial_binning_result.png" width="700" title="Initial binning" alt="Initial binning">
</p>

**Refined binning result**

<p align="center">
  <img src="https://raw.githubusercontent.com/metagentools/gbintk/master/docs/final_GraphBin_binning_result.png" width="700" title="Refined binning result" alt="Refined binning result">
</p>
