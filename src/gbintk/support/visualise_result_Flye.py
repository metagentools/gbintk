#!/usr/bin/python3

"""visualise_result_Flye.py: Visualise the binning result from on the Flye assembly graph.

Visualize the binning result by denoting coloured contigs in the assembly
graph according to their corresponding bins. You can visualise the initial
binning result obtained from an existing binning tool and the final binning
result obtained from GraphBin and compare.

"""

import csv
import logging
import os
import random
import subprocess
import sys
from collections import defaultdict

from graphbin.bidirectionalmap.bidirectionalmap import BidirectionalMap
from igraph import *

__author__ = "Vijini Mallawaarachchi"
__copyright__ = "Copyright 2023-2025, GraphBin-Tk Project"
__credits__ = ["Vijini Mallawaarachchi", "Anuradha Wickramarachchi", "Yu Lin"]
__license__ = "GPL-3.0"
__version__ = "1.0.2"
__maintainer__ = "Vijini Mallawaarachchi"
__email__ = "viji.mallawaarachchi@gmail.com"
__status__ = "Production/Stable"


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
        f"This version of the visualiser makes use of the assembly graph produced by Flye."
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
            readCSV = csv.reader(csvfile, delimiter=",")
            for row in readCSV:
                all_bins_list.append(row[1])

        bins_list = list(set(all_bins_list))
        bins_list.sort()

        n_bins = len(bins_list)
        logger.info("Number of bins available in initial binning result: {n_bins}")

    except:
        logger.error(
            "Please make sure that the correct path to the initial binning result file is provided and it is having the correct format"
        )
        logger.info("Exiting visualiser... Bye...!")
        sys.exit(1)

    logger.info("Constructing the assembly graph...")

    # Get contig names
    # -----------------------------------

    contig_names = BidirectionalMap()

    contig_num = 0

    with open(contig_paths, "r") as file:
        for line in file.readlines():
            if not line.startswith("#"):
                name = line.strip().split()[0]
                contig_names[contig_num] = name
                contig_num += 1

    contig_names_rev = contig_names.inverse

    # Get the paths and edges
    # -----------------------------------

    paths = {}
    segment_contigs = {}

    try:
        with open(contig_paths, mode="r") as file:
            for line in file.readlines():
                if not line.startswith("#"):
                    strings = line.strip().split()

                    contig_name = strings[0]

                    path = strings[-1]
                    path = path.replace("*", "")

                    if path.startswith(","):
                        path = path[1:]

                    if path.endswith(","):
                        path = path[:-1]

                    segments = path.rstrip().split(",")

                    contig_num = contig_names_rev[contig_name]

                    if contig_num not in paths:
                        paths[contig_num] = segments

                    for segment in segments:
                        if segment != "":
                            if segment not in segment_contigs:
                                segment_contigs[segment] = set([contig_num])
                            else:
                                segment_contigs[segment].add(contig_num)

        links_map = defaultdict(set)

        # Get links from assembly_graph.gfa
        with open(assembly_graph_file) as file:
            for line in file.readlines():
                line = line.strip()

                # Identify lines with link information
                if line.startswith("L"):
                    strings = line.split("\t")

                    f1, f2 = "", ""

                    if strings[2] == "+":
                        f1 = strings[1][5:]
                    if strings[2] == "-":
                        f1 = "-" + strings[1][5:]
                    if strings[4] == "+":
                        f2 = strings[3][5:]
                    if strings[4] == "-":
                        f2 = "-" + strings[3][5:]

                    links_map[f1].add(f2)
                    links_map[f2].add(f1)

        # Create list of edges
        edge_list = []

        for i in paths:
            segments = paths[i]

            new_links = []

            for segment in segments:
                my_segment = segment
                my_segment_num = ""

                my_segment_rev = ""

                if my_segment.startswith("-"):
                    my_segment_rev = my_segment[1:]
                    my_segment_num = my_segment[1:]
                else:
                    my_segment_rev = "-" + my_segment
                    my_segment_num = my_segment

                if my_segment in links_map:
                    new_links.extend(list(links_map[my_segment]))

                if my_segment_rev in links_map:
                    new_links.extend(list(links_map[my_segment_rev]))

                if my_segment in segment_contigs:
                    for contig in segment_contigs[my_segment]:
                        if i != contig:
                            # Add edge to list of edges
                            edge_list.append((i, contig))

                if my_segment_rev in segment_contigs:
                    for contig in segment_contigs[my_segment_rev]:
                        if i != contig:
                            # Add edge to list of edges
                            edge_list.append((i, contig))

                if my_segment_num in segment_contigs:
                    for contig in segment_contigs[my_segment_num]:
                        if i != contig:
                            # Add edge to list of edges
                            edge_list.append((i, contig))

            for new_link in new_links:
                if new_link in segment_contigs:
                    for contig in segment_contigs[new_link]:
                        if i != contig:
                            # Add edge to list of edges
                            edge_list.append((i, contig))

                if new_link.startswith("-"):
                    if new_link[1:] in segment_contigs:
                        for contig in segment_contigs[new_link[1:]]:
                            if i != contig:
                                # Add edge to list of edges
                                edge_list.append((i, contig))

        node_count = len(contig_names_rev)

    except:
        logger.error(
            "Please make sure that the correct path to the assembly graph file is provided."
        )
        logger.info("Exiting visuliser... Bye...!")
        sys.exit(1)

    logger.info(f"Total number of contigs available: {node_count}")

    ## Construct the assembly graph
    # -------------------------------

    try:
        # Create the graph
        assembly_graph = Graph()

        # Add vertices
        assembly_graph.add_vertices(node_count)

        # Name vertices
        for i in range(len(assembly_graph.vs)):
            assembly_graph.vs[i]["id"] = i
            assembly_graph.vs[i]["label"] = str(contig_names[i])

        # Add edges to the graph
        assembly_graph.add_edges(edge_list)
        assembly_graph.simplify(multiple=True, loops=False, combine_edges=None)

    except:
        logger.error(
            "Please make sure that the correct path to the assembly graph file is provided."
        )
        logger.info("Exiting GraphBin... Bye...!")
        sys.exit(1)

    logger.info(f"Total number of edges in the assembly graph: {len(edge_list)}")

    # Get initial binning result
    # ----------------------------

    logger.info("Obtaining the initial binning result...")

    bins = [[] for x in range(n_bins)]

    try:
        with open(initial_binning_result, mode="r") as contig_bins:
            readCSV = csv.reader(contig_bins, delimiter=",")
            for row in readCSV:
                contig_num = contig_names_rev[row[0]]

                bin_num = bins_list.index(row[1])
                bins[bin_num].append(contig_num)

        for i in range(n_bins):
            bins[i].sort()

    except:
        logger.error(
            "Please make sure that the correct path to the initial binning result file is provided and it is having the correct format"
        )
        logger.info("Exiting visualiser... Bye...!")
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
        "Drawing and saving the assembly graph with the initial binning result..."
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
            node_colours.append("grey")

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

    logger.info("Obtaining the final GraphBin binning result...")

    bins = [[] for x in range(n_bins)]

    try:
        with open(final_binning_result, mode="r") as contig_bins:
            readCSV = csv.reader(contig_bins, delimiter=",")
            for row in readCSV:
                if row[1] != "unbinned":
                    contig_num = contig_names_rev[row[0]]
                    bin_num = bins_list.index(row[1])
                    bins[bin_num].append(contig_num)

        for i in range(n_bins):
            bins[i].sort()

    except:
        logger.error(
            "Please make sure that the correct path to the final binning result file is provided and it is having the correct format"
        )
        logger.info("Exiting visualiseResult... Bye...!")
        sys.exit(1)

    # Visualise the final assembly graph
    # ------------------------------------

    print(
        "Drawing and saving the assembly graph with the final GraphBin binning result..."
    )

    final_out_fig_name = (
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
            node_colours.append("grey")

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
