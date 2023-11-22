# Archiver

:::: {tab-set}

::: {tab-item} 0.2.0

[![Archiver v0.2.0](badges/release-0.2.0-blue.svg)](https://cloud.sdu.dk/app/jobs/create?app=archiver&version=0.2.0)
![type](badges/type-batch-yellow.svg)
![access](badges/access-open-green.svg)

* **Operating System:** ![](./badges/Ubuntu-22.10-lightseagreen.svg)
* **Terminal:** ![](./badges/tini-0.19.0-lightseagreen.svg) ![](./badges/tmux-3.3a-lightseagreen.svg)
* **Shell:** ![](./badges/bash-5.2.2-lightseagreen.svg) ![](./badges/fish-3.5.1-lightseagreen.svg) ![](./badges/zsh-5.9-lightseagreen.svg)
* **Editor:** ![](./badges/emacs-27.1-lightseagreen.svg) ![](./badges/nano-6.4-lightseagreen.svg) ![](./badges/vim-9.0-lightseagreen.svg)
* **Package Manager:** ![](./badges/apt-2.5.3-lightseagreen.svg) ![](./badges/dpkg-1.21.9-lightseagreen.svg) ![](./badges/npm-8.18.0-lightseagreen.svg) ![](./badges/pip-22.2-lightseagreen.svg)
* **Programming Language:** ![](./badges/GCC-12.2.0-lightseagreen.svg) ![](./badges/Python-3.10.7-lightseagreen.svg) ![](./badges/Python-2.7.18-lightseagreen.svg)
* **Utility:** ![](./badges/Lmod-8.7-lightseagreen.svg)
* **Extension:** ![](./badges/OpenMPI-4.1.4-lightseagreen.svg)

:::

::: {tab-item} 0.1.0

[![Archiver v0.1.0](badges/release-0.1.0-blue.svg)](https://cloud.sdu.dk/app/jobs/create?app=archiver&version=0.1.0)
![type](badges/type-batch-yellow.svg)
![access](badges/access-open-green.svg)

* **Operating System:** ![](./badges/Ubuntu-20.04-lightseagreen.svg)
* **Terminal:** ![](./badges/tmux-3.0a-lightseagreen.svg)
* **Shell:** ![](./badges/bash-5.0.17-lightseagreen.svg)
* **Editor:** ![](./badges/emacs-26.3-lightseagreen.svg) ![](./badges/nano-4.8-lightseagreen.svg) ![](./badges/vim-8.1-lightseagreen.svg)
* **Package Manager:** ![](./badges/apt-2.0.6-lightseagreen.svg) ![](./badges/dpkg-1.19.7-lightseagreen.svg)
* **Programming Language:** ![](./badges/Python-3.8.10-lightseagreen.svg)

:::

::::

This utility is used to submit a batch job that creates a compressed archive file of one or more folders stored on UCloud. Input folders must be added with the parameter _Select additional folders to use_. All mounted folders will be compressed into one single archive file.

``` {note}
The archive utility is configured to use a multi-core compression algorithm, which leverages all the cores available in the selected *machine type*.
```

## Archive format

The compression format can be selected from a list of 7 possibilities using the optional parameter _Archive format_. The available formats are: `7Z`, `BZIP2`, `GZIP`, `TAR`, `WIM`, `XZ`, and `ZIP` (default).

## Terminal session

The _Interactive mode_ parameter is used to start an interactive job session where the user can open the _app terminal interface_ and execute shell commands.
