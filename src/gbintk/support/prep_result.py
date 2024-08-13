#!/usr/bin/python3

"""prep_result.py: Format the initial binning result from an existing binning tool.

Format the initial binning result from an existing binning tool in the .csv format
with contig ID and bin ID. Contigs are numbered starting from 0 and bins are 
numbered starting from 1.

"""


import csv
import logging
import os
import subprocess
import sys

from cogent3.parse.fasta import MinimalFastaParser


__author__ = "Vijini Mallawaarachchi"
__copyright__ = "Copyright 2019-2022, GraphBin-Tk Project"
__credits__ = ["Vijini Mallawaarachchi", "Anuradha Wickramarachchi", "Yu Lin"]
__license__ = "GPL-3.0"
__version__ = "0.1.0"
__maintainer__ = "Vijini Mallawaarachchi"
__email__ = "viji.mallawaarachchi@gmail.com"
__status__ = "Alpha"

# create logger
logger = logging.getLogger(f"GraphBin-Tk {__version__}")


def run(args):
    
    # Get arguments
    assembler = args.assembler
    contig_bins_folder = args.resfolder
    prefix = args.prefix
    delimiter = args.delimiter
    output_path = args.output

    logger.info(f"Welcome to binning results formatter of GraphBin-Tk!")

    logger.info(f"Formatting binning results...")
    logger.info(f"Binning results folder: {contig_bins_folder}")
    logger.info(f"Prefix: {prefix}")
    logger.info(f"Delimiter: {delimiter}")
    logger.info(f"Output path: {output_path}")


    # Get list of files in the folder path of binning result.
    files = os.listdir(contig_bins_folder)


    # Check if folder path of binning result is empty.
    # ---------------------------------------------------
    if len(files) == 0:
        logger.error("Folder containing the initial binning result is empty. Please enter a valid path to the folder.")
        logger.info("Exiting gbintk prepare... Bye...!")
        sys.exit(1)


    # Check if binning result folder contains fasta files.
    # ---------------------------------------------------
    isFasta = True
    for myfile in files:
        if not myfile.lower().endswith((".fasta", ".fa", ".fna")):
            isFasta = False
            break

    if not isFasta:
        logger.error(f"Folder containing the initial binning result does not contain fasta files (.fasta, .fa or .fna).")
        logger.info(f"Exiting gbintk prepare... Bye...!")
        sys.exit(1)

    # Validate prefix
    # ---------------------------------------------------
    if prefix != "":
        if not prefix.endswith("_"):
            prefix = prefix + "_"
    else:
        prefix = ""


    # Format binning results.
    # ---------------------------------------------------

    logger.info(f"Formatting initial binning results")

    contig_bins = []

    for bin_file in files:
        if bin_file.lower().endswith((".fasta", ".fa", ".fna")):
            for contig_name, _ in MinimalFastaParser(f"{contig_bins_folder}/{bin_file}"):
                bin_name = ".".join(bin_file.split(".")[:-1])
                if assembler == "megahit":
                    line = ["_".join(contig_name.split("_")[0:2]), bin_name]
                else:
                    line = [contig_name, bin_name]
                contig_bins.append(line)


    # Write binning results to output file.
    # ---------------------------------------------------

    logger.info(f"Writing initial binning results to output file")

    with open(
        f"{output_path}/{prefix}initial_contig_bins.csv", mode="w"
    ) as contig_bins_file:
        contig_writer = csv.writer(
            contig_bins_file, delimiter=delimiter, quotechar='"', quoting=csv.QUOTE_MINIMAL
        )

        for row in contig_bins:
            contig_writer.writerow(row)

    logger.info(f"Formatted initial binning results can be found at {contig_bins_file.name}")


    # Exit program
    # --------------

    logger.info("Thank you for using binning results formatter for GraphBin-Tk!")


def main(args):
    run(args)

if __name__ == "__main__":
    main()