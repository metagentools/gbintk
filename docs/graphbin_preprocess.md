# Preprocessing for GraphBin

## Assembling and initial binning

Before running GraphBin, you have to assemble our read data into contigs and bin the contigs. Please refer to [assembly instructions](https://gbintk.readthedocs.io/en/latest/metacoag_preprocess/) and [obtaining the binning result](https://gbintk.readthedocs.io/en/latest/metacoag_usage/) provided under MetaCoAG.

Alternatively, you can use other binning tools such as such as [MaxBin2](https://sourceforge.net/projects/maxbin2/), [CONCOCT](https://concoct.readthedocs.io/en/latest/), [MetaBAT2](https://bitbucket.org/berkeleylab/metabat) or [VAMB](https://github.com/RasmussenLab/vamb) to get the initial binning results for your data.

## Formatting the initial binning result

You can use the `prepare` subcommand to format an initial binning result in to the `.csv` format (by default) with contig identifiers and bin ID. Contigs are named according to their original identifier and bins are numbered according to the fasta file name. You can run the `prepare` subcommand as follows.

```shell
# For SPAdes
gbintk prepare --assembler spades ----resfolder /path/to/folder_with_binning_result --output /path/to/output_folder

# For MEGAHIT
gbintk prepare --assembler megahit ----resfolder /path/to/folder_with_binning_result --output /path/to/output_folder

# For Flye
gbintk prepare --assembler flye ----resfolder /path/to/folder_with_binning_result --output /path/to/output_folder
```
More details on the `prepare` subcommand can be found in the [Support](https://gbintk.readthedocs.io/en/latest/prepare/) section of this documentation.

Formatted binning result will be stored in a file named `initial_contig_bins.csv` in the output folder provided.

Now we are all set to run GraphBin.