#!/usr/bin/python3

"""evaluate.py: Evaluate the binning results given a ground truth.

Evaluate the binning results given a ground truth and calculate the
precision, recall, F1-score and ARI of the provided binning result.

"""

import csv
import logging

import scipy.special
from tabulate import tabulate

__author__ = "Vijini Mallawaarachchi"
__copyright__ = "Copyright 2023-2024, GraphBin-Tk Project"
__credits__ = ["Vijini Mallawaarachchi", "Anuradha Wickramarachchi", "Yu Lin"]
__license__ = "GPL-3.0"
__version__ = "1.0.0"
__maintainer__ = "Vijini Mallawaarachchi"
__email__ = "viji.mallawaarachchi@gmail.com"
__status__ = "Production/Stable"

# create logger
logger = logging.getLogger(f"GraphBin-Tk {__version__}")


def run(args):

    # Get paths to binning result and ground truth
    binned_file = args.binned
    ground_truth_file = args.groundtruth
    delimiter = args.delimiter
    prefix = args.prefix
    output_path = args.output

    # Setup output path for log file
    fileHandler = logging.FileHandler(f"{output_path}/gbintk.log")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    fileHandler.setLevel(logging.DEBUG)
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    logger.info(f"Welcome to binning result evaluator of GraphBin-Tk!")

    logger.info(f"Starting binning results evaluation...")
    logger.info(f"Binning results file: {binned_file}")
    logger.info(f"Ground truth file: {ground_truth_file}")
    logger.info(f"Delimiter: {delimiter}")
    logger.info(f"Output path: {output_path}")

    # Validate prefix
    # ---------------------------------------------------
    if prefix != "":
        if not prefix.endswith("_"):
            prefix = prefix + "_"
    else:
        prefix = ""

    # Get the number of bins from the ground truth
    # ---------------------------------------------------------
    ground_truth_n_bins = 0

    all_ground_truth_bins_list = []

    with open(ground_truth_file, mode="r") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=delimiter)
        for row in readCSV:
            all_ground_truth_bins_list.append(row[1])

    ground_truth_bins_list = list(set(all_ground_truth_bins_list))
    ground_truth_n_bins = len(ground_truth_bins_list)

    logger.info(f"Number of bins available in the ground truth: {ground_truth_n_bins}")

    # Get the ground truth
    # ----------------------------
    ground_truth_bins = [[] for x in range(ground_truth_n_bins)]

    ground_truth_count = 0
    ground_truth_bins_1 = {}

    with open(ground_truth_file, mode="r") as contig_bins:
        readCSV = csv.reader(contig_bins, delimiter=delimiter)

        for row in readCSV:
            ground_truth_count += 1
            contig = row[0]
            bin_num = ground_truth_bins_list.index(row[1])
            ground_truth_bins[bin_num].append(contig)
            ground_truth_bins_1[contig] = bin_num

    logger.info(
        f"Number of contigs available in the ground truth: {ground_truth_count}"
    )

    # Get the number of bins from the initial binning result
    # ---------------------------------------------------------
    n_bins = 0

    all_bins_list = []

    with open(binned_file, mode="r") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=delimiter)

        for row in readCSV:
            all_bins_list.append(row[1])

    bins_list = list(set(all_bins_list))
    n_bins = len(bins_list)

    logger.info(f"Number of bins available in the binning result: {n_bins}")

    # Get initial binning result
    # ----------------------------
    bins = [[] for x in range(n_bins)]

    bins_1 = {}

    binned_count = 0
    binned_contigs = []

    with open(binned_file, mode="r") as contig_bins:
        readCSV = csv.reader(contig_bins, delimiter=delimiter)
        for row in readCSV:
            binned_count += 1
            contig = row[0]
            bin_num = bins_list.index(row[1])
            bins[bin_num].append(contig)
            bins_1[contig] = bin_num
            binned_contigs.append(contig)

    logger.info(f"Number of contigs available in the binning result: {binned_count}")

    # Determine precision, recall, F1-score and ARI for binning result
    # ------------------------------------------------------------------

    total_binned = 0

    bins_species = [[0 for x in range(ground_truth_n_bins)] for y in range(n_bins)]

    for i in bins_1:
        if i in ground_truth_bins_1:
            total_binned += 1
            bins_species[bins_1[i]][ground_truth_bins_1[i]] += 1

    logger.info(
        f"Number of contigs available in the binning result that are present in the ground truth: {total_binned}"
    )
    logger.info(
        f"Number of unbinned contigs from the ground truth: {ground_truth_count-total_binned}"
    )

    logger.info(f"Ground truth bin labels:")

    for i in range(len(ground_truth_bins_list)):
        logger.info(f"{i+1}, {ground_truth_bins_list[i]}")

    logger.info(f"KxS Matrix:\n{tabulate(bins_species)}")

    my_precision = getPrecision(bins_species, n_bins, ground_truth_n_bins, total_binned)
    my_recall = getRecall(
        bins_species,
        n_bins,
        ground_truth_n_bins,
        total_binned,
        (ground_truth_count - total_binned),
    )
    my_ari = getARI(bins_species, n_bins, ground_truth_n_bins, total_binned)
    my_f1 = getF1(my_precision, my_recall)

    logger.info(f"Evaluation Results:")
    logger.info(f"Precision = {my_precision*100}")
    logger.info(f"Recall = {my_recall*100}")
    logger.info(f"F1-score = {my_f1*100}")
    logger.info(f"ARI = {my_ari*100}")

    # Write results to output file
    # -----------------------------

    output_file_path = f"{output_path}/{prefix}evaluation_results.txt"

    with open(output_file_path, mode="w") as eval_res:
        eval_res.write(f"KxS Matrix:\n{tabulate(bins_species)}\n")
        eval_res.write(f"Evaluation Results:\n")
        eval_res.write(f"Precision = {my_precision*100}\n")
        eval_res.write(f"Recall = {my_recall*100}\n")
        eval_res.write(f"F1-score = {my_f1*100}\n")
        eval_res.write(f"ARI = {my_ari*100}\n")

    logger.info(f"Evaluation results can be found in {output_file_path}")

    # Exit program
    # --------------

    logger.info(f"Thank you for using binning results evaluator for GraphBin-Tk!")


# Functions to determine precision, recall, F1-score and ARI
# ------------------------------------------------------------


# Get precicion
def getPrecision(mat, k, s, total):
    sum_k = 0
    for i in range(k):
        max_s = 0
        for j in range(s):
            if mat[i][j] > max_s:
                max_s = mat[i][j]
        sum_k += max_s
    return sum_k / total


# Get recall
def getRecall(mat, k, s, total, unclassified):
    sum_s = 0
    for i in range(s):
        max_k = 0
        for j in range(k):
            if mat[j][i] > max_k:
                max_k = mat[j][i]
        sum_s += max_k
    return sum_s / (total + unclassified)


# Get ARI
def getARI(mat, k, s, N):
    t1 = 0
    for i in range(k):
        sum_k = 0
        for j in range(s):
            sum_k += mat[i][j]
        t1 += scipy.special.binom(sum_k, 2)

    t2 = 0
    for i in range(s):
        sum_s = 0
        for j in range(k):
            sum_s += mat[j][i]
        t2 += scipy.special.binom(sum_s, 2)

    t3 = t1 * t2 / scipy.special.binom(N, 2)

    t = 0
    for i in range(k):
        for j in range(s):
            t += scipy.special.binom(mat[i][j], 2)

    ari = (t - t3) / ((t1 + t2) / 2 - t3)
    return ari


# Get F1-score
def getF1(prec, recall):
    return 2 * prec * recall / (prec + recall)


def main(args):
    run(args)


if __name__ == "__main__":
    main()
