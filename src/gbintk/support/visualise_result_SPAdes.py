#!/usr/bin/python3

"""visualise_result_SPAdes.py: Visualise the binning result from on the SPAdes assembly graph.

Visualize the binning result by denoting coloured contigs in the assembly
graph according to their corresponding bins. You can visualise the initial
binning result obtained from an existing binning tool and the final binning
result obtained from GraphBin and compare.

"""

import csv
import logging
import os
import random
import re
import subprocess
import sys
from collections import defaultdict

from graphbin.utils.bidirectionalmap.bidirectionalmap import BidirectionalMap
from igraph import *

__author__ = "Vijini Mallawaarachchi"
__copyright__ = "Copyright 2023-2024, GraphBin-Tk Project"
__credits__ = ["Vijini Mallawaarachchi", "Anuradha Wickramarachchi", "Yu Lin"]
__license__ = "GPL-3.0"
__version__ = "0.1.0"
__maintainer__ = "Vijini Mallawaarachchi"
__email__ = "viji.mallawaarachchi@gmail.com"
__status__ = "Alpha"


# create logger
logger = logging.getLogger(f"GraphBin-Tk {__version__}")


def run(args):

    initial_binning_result = args.initial
    final_binning_result = args.final
    assembly_graph_file = args.graph
    contig_paths = args.paths
    output_path = args.output
    prefix = args.prefix
    dpi = args.dpi
    width = args.width
    height = args.height
    vsize = args.vsize
    lsize = args.lsize
    margin = args.margin
    image_type = args.imgtype
    delimiter = args.delimiter

    logger.info(f"Welcome to binning result visualiser of GraphBin-Tk!")
    logger.info(
        f"This version of the visualiser makes use of the assembly graph produced by SPAdes which is based on the de Bruijn graph approach."
    )

    # Validate prefix
    # ---------------------------------------------------
    try:
        if prefix != "":
            if not prefix.endswith("_"):
                prefix = prefix + "_"
        else:
            prefix = ""

    except:
        logger.error(f"Please enter a valid string for prefix")
        logger.info(f"Exiting visualiser... Bye...!")
        sys.exit(1)

    # Format type if provided
    # ---------------------------------------------------
    if image_type.startswith("."):
        image_type = image_type[1:]

    # Check if output folder exists
    # ---------------------------------------------------

    # Handle for missing trailing forwardslash in output folder path
    if output_path[-1:] != "/":
        output_path = output_path + "/"

    # Create output folder if it does not exist
    if not os.path.isdir(output_path):
        subprocess.run(f"mkdir -p {output_path}", shell=True)

    logger.info(f"Assembly graph file: {assembly_graph_file}")
    logger.info(f"Initial binning results file: {initial_binning_result}")
    logger.info(f"Final binning results file: {final_binning_result}")
    logger.info(f"Final output path: {output_path}")
    logger.info(f"Image type: {image_type}")
    logger.info(f"Width of image: {width} pixels")
    logger.info(f"Height of image: {height} pixels")
    logger.info(f"Size of the vertices: {vsize} pt")
    logger.info(f"Size of the vertex labels: {lsize} pt")
    logger.info(f"Size of the margin: {margin} pt")
    logger.info(f"Delimiter: {delimiter}")

    # Get the number of bins from the initial binning result
    # ---------------------------------------------------

    try:
        all_bins_list = []
        n_bins = 0

        with open(initial_binning_result) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=delimiter)
            for row in readCSV:
                all_bins_list.append(row[1])

        bins_list = list(set(all_bins_list))
        bins_list.sort()

        n_bins = len(bins_list)
        logger.info(f"Number of bins available in initial binning result: {n_bins}")
    except:
        logger.error(
            f"Please make sure that the correct path to the initial binning result file is provided and it is having the correct format"
        )
        logger.info(f"Exiting visualiser... Bye...!")
        sys.exit(1)

    logger.info(f"Constructing the assembly graph...")

    # Get contig paths from contigs.paths
    # -------------------------------------

    paths = {}
    segment_contigs = {}
    node_count = 0

    my_map = BidirectionalMap()

    current_contig_num = ""

    try:
        with open(contig_paths) as file:
            name = file.readline()
            path = file.readline()

            while name != "" and path != "":
                while ";" in path:
                    path = path[:-2] + "," + file.readline()

                start = "NODE_"
                end = "_length_"
                contig_num = str(
                    int(re.search("%s(.*)%s" % (start, end), name).group(1))
                )

                segments = path.rstrip().split(",")

                if current_contig_num != contig_num:
                    my_map[node_count] = int(contig_num)
                    current_contig_num = contig_num
                    node_count += 1

                if contig_num not in paths:
                    paths[contig_num] = [segments[0], segments[-1]]

                for segment in segments:
                    if segment not in segment_contigs:
                        segment_contigs[segment] = set([contig_num])
                    else:
                        segment_contigs[segment].add(contig_num)

                name = file.readline()
                path = file.readline()
    except:
        logger.error(
            f"Please make sure that the correct path to the contig paths file is provided"
        )
        logger.info(f"Exiting visualiser... Bye...!")
        sys.exit(1)

    contigs_map = my_map
    contigs_map_rev = my_map.inverse

    logger.info(f"Total number of contigs available: {node_count}")

    ## Construct the assembly graph
    # -------------------------------

    links = []
    links_map = defaultdict(set)

    try:
        # Get links from assembly_graph_with_scaffolds.gfa
        with open(assembly_graph_file) as file:
            for line in file.readlines():
                line = line.strip()

                # Identify lines with link information
                if line.startswith("L"):
                    strings = line.split("\t")
                    f1, f2 = strings[1] + strings[2], strings[3] + strings[4]
                    links_map[f1].add(f2)
                    links_map[f2].add(f1)
                    links.append(
                        strings[1] + strings[2] + " " + strings[3] + strings[4]
                    )

        # Create graph
        assembly_graph = Graph()

        # Add vertices
        assembly_graph.add_vertices(node_count)

        # Create list of edges
        edge_list = []

        # Name vertices
        for i in range(node_count):
            assembly_graph.vs[i]["id"] = i
            assembly_graph.vs[i]["label"] = "NODE_" + str(contigs_map[i])

        for i in range(len(paths)):
            segments = paths[str(contigs_map[i])]

            start = segments[0]
            start_rev = ""

            if start.endswith("+"):
                start_rev = start[:-1] + "-"
            else:
                start_rev = start[:-1] + "+"

            end = segments[1]
            end_rev = ""

            if end.endswith("+"):
                end_rev = end[:-1] + "-"
            else:
                end_rev = end[:-1] + "+"

            new_links = []

            if start in links_map:
                new_links.extend(list(links_map[start]))
            if start_rev in links_map:
                new_links.extend(list(links_map[start_rev]))
            if end in links_map:
                new_links.extend(list(links_map[end]))
            if end_rev in links_map:
                new_links.extend(list(links_map[end_rev]))

            for new_link in new_links:
                if new_link in segment_contigs:
                    for contig in segment_contigs[new_link]:
                        if i != contigs_map_rev[int(contig)]:
                            # Add edge to list of edges
                            edge_list.append((i, contigs_map_rev[int(contig)]))

        # Add edges to the graph
        assembly_graph.add_edges(edge_list)
        assembly_graph.simplify(multiple=True, loops=False, combine_edges=None)
    except:
        logger.error(
            f"Please make sure that the correct path to the assembly graph file is provided"
        )
        logger.info("Exiting visualiser... Bye...!")
        sys.exit(1)

    # Get the number of bins from the initial binning result
    # ---------------------------------------------------

    n_bins = 0

    try:
        all_bins_list = []

        with open(initial_binning_result) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=delimiter)
            for row in readCSV:
                all_bins_list.append(row[1])

        bins_list = list(set(all_bins_list))
        bins_list.sort()

        n_bins = len(bins_list)
        logger.info(f"Number of bins available in the initial binning result: {n_bins}")
    except:
        logger.error(
            f"Please make sure that the correct path to the initial binning result file is provided and it is having the correct format."
        )
        logger.info(f"Exiting visualiser... Bye...!")
        sys.exit(1)

    # Get initial binning result
    # ----------------------------

    logger.info(f"Obtaining the initial binning result...")

    bins = [[] for x in range(n_bins)]

    try:
        with open(initial_binning_result) as contig_bins:
            readCSV = csv.reader(contig_bins, delimiter=delimiter)
            for row in readCSV:
                start = "NODE_"
                end = "_length_"
                contig_num = contigs_map_rev[
                    int(re.search("%s(.*)%s" % (start, end), row[0]).group(1))
                ]

                bin_num = bins_list.index(row[1])
                bins[bin_num].append(contig_num)

        for i in range(n_bins):
            bins[i].sort()

    except:
        logger.error(
            f"Please make sure that the correct path to the binning result file is provided and it is having the correct format"
        )
        logger.info(f"Exiting visualiser... Bye...!")
        sys.exit(1)

    # Get list of colours according to number of bins
    # -------------------------------------------------

    logger.info(f"Picking colours out of 22 supported colours...")

    my_colours = [
        "#e6194b",
        "#3cb44b",
        "#ffe119",
        "#4363d8",
        "#f58231",
        "#911eb4",
        "#46f0f0",
        "#f032e6",
        "#bcf60c",
        "#fabebe",
        "#008080",
        "#e6beff",
        "#9a6324",
        "#fffac8",
        "#800000",
        "#aaffc3",
        "#808000",
        "#ffd8b1",
        "#000075",
        "#808080",
        "#ffffff",
        "#000000",
    ]

    # Visualise the initial assembly graph
    # --------------------------------------

    logger.info(
        f"Drawing and saving the assembly graph with the initial binning result..."
    )

    initial_out_fig_name = f"{output_path}{prefix}initial_binning_result.{image_type}"

    node_colours = []

    for i in range(node_count):
        no_bin = True
        for j in range(n_bins):
            if i in bins[j]:
                node_colours.append(my_colours[j])
                no_bin = False

        if no_bin:
            node_colours.append("white")

    assembly_graph.vs["color"] = node_colours

    visual_style = {}

    # Set bbox and margin
    visual_style["bbox"] = (width, height)
    visual_style["margin"] = margin

    # Set vertex size
    visual_style["vertex_size"] = vsize

    # Set vertex lable size
    visual_style["vertex_label_size"] = lsize

    # Don't curve the edges
    visual_style["edge_curved"] = False

    # Set the layout
    my_layout = assembly_graph.layout_fruchterman_reingold()
    visual_style["layout"] = my_layout

    # Plot the graph
    plot(assembly_graph, initial_out_fig_name, **visual_style)

    # Get the final GraphBin binning result
    # ---------------------------------------

    logger.info(f"Obtaining the final GraphBin binning result...")

    bins = [[] for x in range(n_bins)]

    try:
        with open(final_binning_result) as contig_bins:
            readCSV = csv.reader(contig_bins, delimiter=delimiter)
            for row in readCSV:
                if row[1] != "unbinned":
                    bin_num = bins_list.index(row[1])

                    start = "NODE_"
                    end = "_length_"
                    contig_num = contigs_map_rev[
                        int(re.search("%s(.*)%s" % (start, end), row[0]).group(1))
                    ]

                    bins[bin_num].append(contig_num)

        for i in range(n_bins):
            bins[i].sort()

    except:
        logger.error(
            f"Please make sure that the correct path to the final binning result file is provided and it is having the correct format"
        )
        logger.info(f"Exiting visualiser... Bye...!")
        sys.exit(1)

    # Visualise the final assembly graph
    # ------------------------------------

    logger.info(
        f"Drawing and saving the assembly graph with the final GraphBin binning result..."
    )

    final_out_fig_name = final_out_fig_name = (
        f"{output_path}{prefix}final_GraphBin_binning_result.{image_type}"
    )

    node_colours = []

    for i in range(node_count):
        no_bin = True
        for j in range(n_bins):
            if i in bins[j]:
                node_colours.append(my_colours[j])
                no_bin = False

        if no_bin:
            node_colours.append("white")

    assembly_graph.vs["color"] = node_colours

    visual_style = {}

    # Set bbox and margin
    visual_style["bbox"] = (width, height)
    visual_style["margin"] = margin

    # Set vertex size
    visual_style["vertex_size"] = vsize

    # Set vertex lable size
    visual_style["vertex_label_size"] = lsize

    # Don't curve the edges
    visual_style["edge_curved"] = False

    # Set the layout
    visual_style["layout"] = my_layout

    # Plot the graph
    plot(assembly_graph, final_out_fig_name, **visual_style)

    logger.info(
        f"Visualization of the initial binning results can be found at {initial_out_fig_name}"
    )
    logger.info(
        f"Visualization of the final GraphBin binning results can be found at {final_out_fig_name}"
    )

    # Exit program
    # --------------

    logger.info(f"Thank you for using visualiser for GraphBin-Tk!")


def main(args):
    run(args)


if __name__ == "__main__":
    main()
