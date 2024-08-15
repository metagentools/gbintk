# Evaluating binning results

You can use the `evaluate` subcommand to evaluate your binning results given a ground truth.

Run `gbintk evaluate --help` or `gbintk evaluate -h` to list the help message for evaluation.

```shell
Usage: gbintk evaluate [OPTIONS]

  Evaluate the binning results given a ground truth

Options:
  --binned PATH            path to the .csv file with the initial binning
                           output from an existing tool  [required]
  --groundtruth PATH       path to the .csv file with the ground truth
                           [required]
  --delimiter [,|;|     |" "]  delimiter for input/output results. Supports a
                           comma (,), a semicolon (;), a tab ($'\t'), a space
                           (" ") and a pipe (|)  [default: ,]
  --output PATH            path to the output folder  [required]
  -h, --help               Show this message and exit.
```

## Input Format

`visualise` subcommand takes in 2 files as inputs.

* Binning result containing the comma separated records of `contig id,bin number` (in `.csv` format)
* Ground truth annotations containing the comma separated records of `contig id, groud truth bin` (in `.csv` format)

## Example Usage

```shell
gbintk evaluate --binned /path/to/binning_res.csv --groundtruth /path/to/grouhdtruth.csv --output /path/to/output_folder
```

## Output

You will get a file named `evaluation_results.txt` that contains the confusion matrix and the evaluation metrics precition, recall, F1-score and adjusted rand index (ARI). 

Please refer to the supplementary material of the [GraphBin publication](https://doi.org/10.1093/bioinformatics/btaa180) for further details on the confusion matrix and the evaluation metrics.