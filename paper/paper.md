---
title: 'GraphBin-Tk: assembly graph-based metagenomic binning toolkit'
tags:
  - Python
  - bioinformatics
  - metagenomics
  - binning
  - contigs
authors:
  - name: Vijini Mallawaarachchi
    orcid: 0000-0002-2651-8719
    corresponding: true
    affiliation: 1
  - name: Anuradha Wickramarachchi
    orcid: 0000-0003-4160-5965
    affiliation: 2
  - name: Robert McArthur
    orcid: 0000-0001-9099-339X
    affiliation: 3
  - name: Yapeng Lang
    orcid: 0009-0001-6828-0964
    affiliation: 3
  - name: Katherine Caley
    orcid: 0000-0002-8459-6168
    affiliation: 3
  - name: Gavin Huttley
    orcid: 0000-0001-7224-2074
    affiliation: 3
affiliations:
 - name: Flinders Accelerator for Microbiome Exploration, College of Science and Engineering, Flinders University, Bedford Park, Adelaide, SA 5042, Australia
   index: 1
 - name: Australian e-Health Research Centre, Commonwealth Scientific and Industrial Research Organisation (CSIRO), Westmead, NSW 2145, Australia
   index: 2
 - name: Research School of Biology, The Australian National University, Canberra, ACT 2601, Australia
   index: 3
date: 15 August 2024
bibliography: paper.bib

---

# Summary

The study of genetic material directly obtained from natural environments, termed metagenomics, offers valuable insights into microbial communities and their impact on human health and environmental dynamics [@Edwards:2013; @Pargin:2023]. Once the genetic material is extracted, sequenced to obtain reads and assembled to obtain contigs, a process known as metagenomic binning is used to cluster contigs into bins that represent different taxonomic groups which results in draft microbial genomes or metagenome-assembled genomes (MAGs) [@Mallawaarachchi:2024]. Several automated metagenomic binning tools incorporating novel computational methods have been introduced [@Alneberg:2014; @Wu:2015; @Kang:2019; @Xue:2022; @Chandrasiri:2022; @Pan:2023; @Xue:2024] which have led to the discovery and characterisation of many novel micro-organisms [@Brooks:2017; @Kang:2024].

Conventional metagenomic binning tools make use of features such as nucleotide composition and abundance information of contigs, yet find it challenging to bin sequences of closely related species and sequences that have noisy features. Binning tools, such as MetaCoAG [@Mallawaarachchi1:2022; @Mallawaarachchi2:2022] that use metagenome assembly graphs (a structure containing the connectivity information of contigs) are gaining popularity due to their improved binning results over conventional binning methods. Moreover, assembly graph-based bin refinement tools such as GraphBin [@Mallawaarachchi1:2020] and GraphBin2 [@Mallawaarachchi2:2020; @Mallawaarachchi:2021] have been introduced to refine binning results from existing binning tools. Yet, these tools exist as individual software and running them individually can be complex, time-consuming and less accessible. Here we present GraphBin-Tk, an assembly graph-based metagenomic binning tool that combines the capabilities of MetaCoAG, GraphBin and GraphBin2, along with additional pre-processing and post-processing functionality into one comprehensive toolkit. GraphBin-Tk is hosted at [https://github.com/metagentools/gbintk](https://github.com/metagentools/gbintk).

# Statement of need

It is crucial to obtain accurate binning results in metagenomic studies to understand the composition and functional potential of microbial communities. Conventional binning methods mainly rely on two features of contigs; 1) nucleotide composition, represented as normalised frequencies of oligonucleotides (short substrings of a particular length) and 2) abundance, the average number of reads that covers each nucleotide base of the contig [@Mallawaarachchi:2024]. Previous studies have found that these tools face several challenges when binning complex datasets, especially those containing closely related species, short sequences, and shared genomic regions [@Mallawaarachchi:2024].

To address these challenges, several graph-based metagenomic binning tools [@Mallawaarachchi:2024] such as MetaCoAG [@Mallawaarachchi1:2022; @Mallawaarachchi2:2022] and GraphMB [@Lamurias:2022], and bin refinement tools such as GraphBin [@Mallawaarachchi1:2020] and GraphBin2 [@Mallawaarachchi2:2020; @Mallawaarachchi:2021] have been developed. These tools enhance the binning results by leveraging the connectivity information of the assembly graph -- an intermediate output generated from the assembly process, that is often discarded during downstream analysis. However, running these tools individually can be challenging. Users have to install and configure multiple software packages, resolve dependencies and manage different file formats, which raises the risk of errors. Furthermore, existing metagenomic binning toolkits and wrappers such as MetaWRAP [@Uritskiy:2018], DAS Tool [@Sieber:2018] and MetaBinner [@Wang:2023] aim to simplify metagenomic binning workflows, but they do not incorporate graph-based binning tools.

GraphBin-Tk addresses the aforementioned challenges by integrating the capabilities of GraphBin [@Mallawaarachchi1:2020], GraphBin2 [@Mallawaarachchi2:2020; @Mallawaarachchi:2021] and MetaCoAG [@Mallawaarachchi1:2022; @Mallawaarachchi2:2022] in a comprehensive toolkit for metagenomic binning and refinement as shown in \autoref{fig1}. Once a metagenomic assembly is obtained, GraphBin-Tk enables researchers to bin contigs, refine bins and provides additional features such as visualisation and evaluation, enabling a wider range of tasks to be performed seamlessly without needing to install and execute additional software. GraphBin-Tk also eliminates any compatibility issues that may arise from running separate binning-related software and enhances the user experience by making the software easier to learn and use.

![Example binning workflow using tools available from GraphBin-Tk.\label{fig1}](gbintk_workflow.svg){width=100%}

# Functionality

GraphBin-Tk can perform stand-alone metagenomic binning using MetaCoAG and bin refinement using either GraphBin or GraphBin2. Additionally, pre- and post-processing functionalities to run these tools and analyse the produced results are included. GraphBin-Tk can be launched using the command `gbintk`. A list of the subcommands provided in GraphBin-Tk is as follows. Further details about the subcommands can be found in the GraphBin-Tk documentation at [https://gbintk.readthedocs.io/](https://gbintk.readthedocs.io/).

| Subcommand   | Tool/processing functionality                                       | Inputs required                                                              |
 |:------------:|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
 | `graphbin`   | Bin refinement tool GraphBin                                        | Contigs, assembly graph file(s), initial binning result                  |
 | `graphbin2`  | Bin refinement tool GraphBin2                                       | Contigs, assembly graph file(s), initial binning result, coverage of contigs |
 | `metacoag`   | Binning tool MetaCoAG                                               | Contigs, assembly graph file(s), coverage of contigs                         |
 | `prepare`    | Format initial binning results for GraphBin and GraphBin2           | Folder containing the initial binning result                                 |
 | `visualise`  | Visualise initial and refined binning results on the assembly graph | Assembly graph file(s), initial binning result, final binning result         |
 | `evaluate`   | Evaluate binning results given a ground truth                       | Binning result, ground truth                                                 |

After assembling a metagenomic dataset, a user can start the analysis by running the `metacoag` subcommand to bin the resulting contigs and obtain MAGs as shown in \autoref{fig1}. GraphBin-Tk supports metagenome assemblies generated from three popular metagenome assemblers; metaSPAdes [@Nurk:2017] and MEGAHIT [@Li:2015] for short-read sequencing data and metaFlye [@Kolmogorov:2020] for long-read sequencing data. The MetaCoAG binning result can be formatted using the `prepare` subcommand into a delimited text file such as `.csv` or `.tsv` that represents each contig and its bin name. This formatted binning result can be improved by providing to either GraphBin or GraphBin2 using the subcommands `graphbin` or `graphbin2` with the contigs file, the assembly graph files and the read coverage of contigs (\autoref{fig1}).

The initial MetaCoAG binning result and the refined binning result can be visualised on the assembly graph using the `visualise` subcommand  (\autoref{fig1}). Users can generate images in different formats such as `png`, `eps`, `pdf` and `svg`, and customise the dimensions of the images. An example is shown in \autoref{fig2} for the Sim-5G+metaSPAdes dataset [@Mallawaarachchi2:2020; @Mallawaarachchi:2021] containing five bacterial species. 

![Visualisation of the assembly graph with the initial binning result from MetaCoAG (left) and final binning result from GraphBin (right) for the Sim-5G+metaSPAdes dataset. The vertices represent contigs and edges represent connections in the assembly graph. The five colours represent the five bins and the white vertices represent unbinned contigs.\label{fig2}](visualisation.svg){width=100%}

Finally, the produced binning results can be evaluated using the `evaluate` subcommand by providing the ground truth bins of contigs (\autoref{fig1}). This evaluation is possible only for simulated or mock metagenomes where the ground truth genomes of contigs are known. GraphBin-Tk uses the four common metrics 1) precision, 2) recall, 3) F1-score and 4) Adjusted Rand Index (ARI) that have been used in previous binning studies [@Alneberg:2014; @Meyer:2018; @Mallawaarachchi1:2020]. These metrics can be plotted for comparison between the initial binning result and the refined binning result using custom code as shown in \autoref{fig3}.

![Comparison of evaluation metrics for the initial binning result from MetaCoAG and the refined binning result from GraphBin for the Sim-5G+metaSPAdes dataset.\label{fig3}](gbintk_metrics_comparison.svg){width=70%}

Please refer to the original publications of GraphBin [@Mallawaarachchi1:2020], GraphBin2 [@Mallawaarachchi2:2020; @Mallawaarachchi:2021] and MetaCoAG [@Mallawaarachchi1:2022; @Mallawaarachchi2:2022] for detailed benchmarking results of each tool.


# Availability

GraphBin-Tk is distributed as a Conda package available in the Bioconda channel [@Gruning:2018] at [https://anaconda.org/bioconda/gbintk](https://anaconda.org/bioconda/gbintk). GraphBin-Tk is also available as a Python package on PyPI at [https://pypi.org/project/gbintk](https://pypi.org/project/gbintk/). The source code is available on GitHub at [https://github.com/metagentools/gbintk](https://github.com/metagentools/gbintk) and features continuous integration, testing coverage, and continuous deployment using GitHub actions. Detailed documentation and example usage can be found at [https://gbintk.readthedocs.io/](https://gbintk.readthedocs.io/).

# Acknowledgements

This work is dedicated to the memory of the late Dr Yu Lin (The Australian National University) whose guidance and support were instrumental in shaping the original work. His wisdom and mentorship are deeply missed. 

This work was supported by an Essential Open Source Software for Science Grant EOSS5-0000000223 from the Chan Zuckerberg Initiative. This work was undertaken with the assistance of resources and services from the National Computational Infrastructure (NCI Australia) which is supported by the Australian Government. 


# References

