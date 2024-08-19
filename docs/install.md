# Installing GraphBin-Tk

```shell
# clone repository
git clone https://github.com/metagentools/gbintk.git

# move to gbintk directory
cd gbintk

# create and activate conda env
conda env create -f environment.yml
conda activate gbintk

# install using flit
flit install

# test installation
gbintk --help
```