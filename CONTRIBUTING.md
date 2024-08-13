# Contributing to GraphBin-Tk project

We love to have your contributions to the GraphBin-Tk project, whether it's:
* Reporting a bug
* Submitting a fix
* Proposing new features

## Clone and install GraphBin-Tk onto your machine

First, make sure you have [git](https://github.com/git-guides/install-git) installed on your machine.

On GitHub, [fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) the GraphBin-Tk repository and [clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) it to your machine.

```shell
# clone repository to your local machine
git clone https://github.com/metagentools/gbintk.git
```

Move to the `gbintk` directory and install `gbintk` via [flit](https://pypi.org/project/flit/).

```shell
# go to repo direcotry
cd gbintk

# install flit
pip install flit

# install graphbin via flit
flit install -s --python `which python`
```

## Test `gbintk` installation

Use the following command to run [pytest](https://docs.pytest.org/en/7.1.x/) and the all the tests should pass.

```shell
pytest
```

## Coding Style

We adhere to the [PEP 8](https://peps.python.org/pep-0008/) style guide. 

Before committing, make sure to run [`black`](https://pypi.org/project/black/) and [`isort`](https://pypi.org/project/isort/).

```shell
# run black
black src/

# run isort
isort src/ --atomic 
```

## Report bugs using Github's issues

We use GitHub issues to track public bugs. Report a bug by opening a new issue in GitHub [issues](https://github.com/metagentools/gbintk/issues). You will get to select between templates for bug report and feature request.

## Committing code

Once you have finished coding and all the tests pass, commit your code and make a pull request. 

```shell
# Add changed/added files
git add <file name>

# Commit changes
git commit -m "<commit message>"

# Push changes
git push
```

Make sure to follow the commit style of [c3dev](https://github.com/cogent3/c3dev/wiki#style-for-commit-messages). Relevant prefixes are replicated below for convenience.

| **Commit Prefix** | **For**                                       |
|-------------------|-----------------------------------------------|
| DEV:              | development tool or utility                   |
| DOC:              | documentation                                 |
| TST:              | addition or modification of tests             |
| REL:              | related to a release                          |
| MAINT:            | maintenance commit (refactoring, typos, etc.) |
| BUG:              | bug fix                                       |
| GIT:              | git related                                   |
| REV:              | revert an earlier commit                      |


Your contribution will be reviewed before accepting it. 

## License

By contributing, you agree that your contributions will be licensed under the [GPL-3.0](https://github.com/metagentools/gbintk/blob/main/LICENSE) License.

## References

This document was adapted from the open-source contribution guidelines for [Transcriptase](https://github.com/briandk/transcriptase-atom/blob/master/CONTRIBUTING.md) and [c3dev](https://github.com/cogent3/c3dev/wiki/How-to-Contribute-Code).
