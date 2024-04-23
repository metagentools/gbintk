#!/usr/bin/env python3

from collections import OrderedDict
from typing import Mapping, Optional

import click

__author__ = "Vijini Mallawaarachchi"
__copyright__ = "Copyright 2019-2022, GraphBin-Tk Project"
__credits__ = ["Vijini Mallawaarachchi", "Anuradha Wickramarachchi", "Yu Lin"]
__license__ = "GPL-3.0"
__version__ = "0.1.0"
__maintainer__ = "Vijini Mallawaarachchi"
__email__ = "viji.mallawaarachchi@gmail.com"
__status__ = "Alpha"


class OrderedGroup(click.Group):
    """custom group class to ensure help function returns commands in desired order.
    class is adapted from Максим Стукало's answer to
    https://stackoverflow.com/questions/47972638/how-can-i-define-the-order-of-click-sub-commands-in-help
    """

    def __init__(
        self,
        name: Optional[str] = None,
        commands: Optional[Mapping[str, click.Command]] = None,
        **kwargs,
    ):
        super().__init__(name, commands, **kwargs)
        #: the registered subcommands by their exported names.
        self.commands = commands or OrderedDict()

    def list_commands(self, ctx: click.Context) -> Mapping[str, click.Command]:
        return self.commands


@click.group(
    cls=OrderedGroup, context_settings=dict(help_option_names=["-h", "--help"])
)
@click.version_option(__version__, "-v", "--version", is_flag=True)
def main():
    """gbintk (GraphBin-Tk): Assembly graph-based metagenomic binning toolkit"""
    pass


_assembler = click.option(
    "--assembler",
    help="name of the assembler used (SPAdes, SGA, MEGAHIT or Flye)",
    type=click.Choice(["spades", "sga", "megahit", "flye"], case_sensitive=False),
    required=True,
)
_graph = click.option(
    "--graph",
    help="path to the assembly graph file",
    type=click.Path(exists=True),
    required=True,
)
_contigs = click.option(
    "--contigs",
    help="path to the contigs file",
    type=click.Path(exists=True),
    required=True,
)
_paths = click.option(
    "--paths",
    help="path to the contigs.paths (metaSPAdes) or assembly.info (metaFlye) file",
    type=click.Path(exists=True),
    required=False,
)
_abundance = click.option(
    "--abundance",
    help="path to the abundance file",
    type=click.Path(exists=True),
    required=True,
)
_binned = click.option(
    "--binned",
    help="path to the .csv file with the initial binning output from an existing tool",
    type=click.Path(exists=True),
    required=True,
)
_output = click.option(
    "--output",
    help="path to the output folder",
    type=click.Path(dir_okay=True, writable=True, readable=True),
    required=True,
)
_prefix = click.option(
    "--prefix",
    help="prefix for the output file",
    type=str,
    required=False,
)
_delimiter = click.option(
    "--delimiter",
    help="delimiter for input/output results. Supports a comma (,), a semicolon (;), a tab ($'\\t'), a space (\" \") and a pipe (|)",
    type=click.Choice([",", ";", "$'\\t'", '" "'], case_sensitive=False),
    default=",",
    show_default=True,
    required=False,
)
_nthreads = click.option(
    "--nthreads",
    help="number of threads to use.",
    type=int,
    default=8,
    show_default=True,
    required=False,
)


_click_command_opts = dict(
    no_args_is_help=True, context_settings={"show_default": True}
)


# Main GraphBin
# -------------------------------------------------------------------
@main.command(**_click_command_opts)
@_assembler
@_graph
@_contigs
@_paths
@_binned
@_output
@_prefix
@click.option(
    "--max_iteration",
    help="maximum number of iterations for label propagation algorithm",
    type=int,
    default=100,
    show_default=True,
    required=False,
)
@click.option(
    "--diff_threshold",
    help="difference threshold for label propagation algorithm",
    type=click.FloatRange(0, 1),
    default=0.1,
    show_default=True,
    required=False,
)
@_delimiter
def graphbin(
    assembler,
    graph,
    contigs,
    paths,
    binned,
    output,
    prefix,
    max_iteration,
    diff_threshold,
    delimiter,
):
    """GraphBin: Refined Binning of Metagenomic Contigs using Assembly Graphs"""

    print("Run GraphBin...")
    from graphbin.utils import (
        graphbin_Canu,
        graphbin_Flye,
        graphbin_MEGAHIT,
        graphbin_Miniasm,
        graphbin_SGA,
        graphbin_SPAdes,
    )

    class ArgsObj:
        def __init__(
            self,
            assembler,
            graph,
            contigs,
            paths,
            binned,
            output,
            prefix,
            max_iteration,
            diff_threshold,
            delimiter,
        ):
            self.assembler = assembler
            self.graph = graph
            self.contigs = contigs
            self.paths = paths
            self.binned = binned
            self.output = output
            self.prefix = prefix
            self.max_iteration = max_iteration
            self.diff_threshold = diff_threshold
            self.delimiter = delimiter

    # Make args object
    args = ArgsObj(
        assembler,
        graph,
        contigs,
        paths,
        binned,
        output,
        prefix,
        max_iteration,
        diff_threshold,
        delimiter,
    )

    # Run GraphBin
    # ---------------------------------------------------
    if assembler.lower() == "canu":
        graphbin_Canu.main(args)
    if assembler.lower() == "flye":
        graphbin_Flye.main(args)
    if assembler.lower() == "megahit":
        graphbin_MEGAHIT.main(args)
    if assembler.lower() == "miniasm":
        graphbin_Miniasm.main(args)
    if assembler.lower() == "sga":
        graphbin_SGA.main(args)
    if assembler.lower() == "spades":
        graphbin_SPAdes.main(args)

# Main GraphBin2
# -------------------------------------------------------------------
@main.command(**_click_command_opts)
@_assembler
@_graph
@_contigs
@_paths
@click.option(
    "--abundance",
    help="path to the abundance file",
    type=click.Path(exists=True),
    required=True,
)
@_binned
@_output
@_prefix
@click.option(
    "--depthb",
    help="maximum depth for the breadth-first-search.",
    type=int,
    default=5,
    show_default=True,
    required=False,
)
@click.option(
    "--threshold",
    help="threshold for determining inconsistent vertices.",
    type=float,
    default=1.5,
    show_default=True,
    required=False,
)
@_delimiter
@_nthreads
def graphbin2(
    assembler,
    graph,
    contigs,
    paths,
    abundance,
    binned,
    output,
    prefix,
    depthb,
    threshold,
    delimiter,
    nthreads,
):
    """GraphBin2: Refined and Overlapped Binning of Metagenomic Contigs Using Assembly Graphs"""

    print("Run GraphBin2...")


# Main MetaCoAG
# -------------------------------------------------------------------
@main.command(**_click_command_opts)
@_assembler
@_graph
@_contigs
@_paths
@_abundance
@_output
@click.option(
    "--hmm",
    help="path to marker.hmm file.",
    default="auxiliary/marker.hmm",
    show_default=True,
    type=str,
    required=False,
)
@_prefix
@click.option(
    "--min_length",
    help="minimum length of contigs to consider for binning.",
    type=int,
    default=1000,
    show_default=True,
    required=False,
)
@click.option(
    "--p_intra",
    help="minimum probability of an edge matching to assign to the same bin.",
    type=click.FloatRange(0, 1),
    default=0.1,
    show_default=True,
    required=False,
)
@click.option(
    "--p_inter",
    help="maximum probability of an edge matching to create a new bin.",
    type=click.FloatRange(0, 1),
    default=0.01,
    show_default=True,
    required=False,
)
@click.option(
    "--d_limit",
    help="distance limit for contig matching.",
    type=int,
    default=20,
    show_default=True,
    required=False,
)
@click.option(
    "--depthlp",
    help="depth to consider for label propagation.",
    type=int,
    default=10,
    show_default=True,
    required=False,
)
@click.option(
    "--n_mg",
    help="total number of marker genes.",
    type=int,
    default=108,
    show_default=True,
    required=False,
)
@click.option(
    "--no_cut_tc",
    help="do not use --cut_tc for hmmsearch.",
    is_flag=True,
    default=False,
    show_default=True,
    required=False,
)
@click.option(
    "--mg_threshold",
    help="length threshold to consider marker genes.",
    type=click.FloatRange(0, 1, clamp=True),
    default=0.5,
    show_default=True,
    required=False,
)
@click.option(
    "--bin_mg_threshold",
    help="minimum fraction of marker genes that should be present in a bin.",
    type=click.FloatRange(0, 1, clamp=True),
    default=0.33333,
    show_default=True,
    required=False,
)
@click.option(
    "--min_bin_size",
    help="minimum size of a bin to output in base pairs (bp).",
    type=int,
    default=200000,
    show_default=True,
    required=False,
)
@_delimiter
@_nthreads
def metacoag(
    assembler,
    graph,
    contigs,
    paths,
    abundance,
    output,
    hmm,
    prefix,
    min_length,
    p_intra,
    p_inter,
    d_limit,
    depthlp,
    n_mg,
    no_cut_tc,
    mg_threshold,
    bin_mg_threshold,
    min_bin_size,
    delimiter,
    nthreads,
):
    """MetaCoAG: Binning Metagenomic Contigs via Composition, Coverage and Assembly Graphs"""

    print("Run MetaCoAG...")
