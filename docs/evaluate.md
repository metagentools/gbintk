# Evaluating binning results

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