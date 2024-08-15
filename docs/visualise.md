# Visualising binning results

Run `gbintk visualise --help` or `gbintk visualise -h` to list the help message for visualisation.

```shell
Usage: gbintk visualise [OPTIONS]

  Visualise binning and refinement results

Options:
  --assembler [spades|megahit|flye]
                                  name of the assembler used (SPAdes, MEGAHIT
                                  or Flye)  [required]
  --initial PATH                  path to the initial binning result
                                  [required]
  --final PATH                    path to the final binning result  [required]
  --graph PATH                    path to the assembly graph file  [required]
  --paths PATH                    path to the contigs.paths (metaSPAdes) or
                                  assembly.info (metaFlye) file
  --output PATH                   path to the output folder  [required]
  --prefix TEXT                   prefix for the output file
  --dpi INTEGER                   dpi value  [default: 300]
  --width INTEGER                 width of the image in pixels  [default:
                                  2000]
  --height INTEGER                height of the image in pixels  [default:
                                  2000]
  --vsize INTEGER                 size of the vertices  [default: 50]
  --lsize INTEGER                 size of the vertex labels  [default: 8]
  --margin INTEGER                margin of the figure  [default: 50]
  --type TEXT                     type of the image (jpg, png, eps, svg)
                                  [default: png]
  --delimiter [,|;|$'\t'|" "]     delimiter for input/output results. Supports
                                  a comma (,), a semicolon (;), a tab ($'\t'),
                                  a space (" ") and a pipe (|)  [default: ,]
  -h, --help                      Show this message and exit.
```