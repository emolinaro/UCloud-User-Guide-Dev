# Charticulator

:::: {tab-set}

::: {tab-item} 2.2.0

[![charticulator](badges/release-2.2.0-blue.svg)](https://cloud.sdu.dk/app/jobs/create?app=charticulator&version=2.2.0)
![type](badges/type-interactive-yellow.svg)
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

::: {tab-item} 2.0.4

[![charticulator](badges/release-2.0.4-blue.svg)](https://cloud.sdu.dk/app/jobs/create?app=charticulator&version=2.0.4)
![type](badges/type-interactive-yellow.svg)
![access](badges/access-open-green.svg)

* **Operating System:** ![](./badges/Ubuntu-18.04-lightseagreen.svg)
* **Shell:** ![](./badges/bash-4.4.20-lightseagreen.svg)
* **Editor:** ![](./badges/emacs-25.2.2-lightseagreen.svg) ![](./badges/nano-2.9.3-lightseagreen.svg) ![](./badges/vim-8.0-lightseagreen.svg)
* **Package Manager:** ![](./badges/apt-1.6.14-lightseagreen.svg) ![](./badges/dpkg-1.19.0.5-lightseagreen.svg) ![](./badges/npm-6.14.12-lightseagreen.svg)
* **Programming Language:** ![](./badges/Python-3.6.9-lightseagreen.svg) ![](./badges/Python-2.7.17-lightseagreen.svg)

:::

::::

Charticulator is a new charting tool that allows you to design charts by interactively specifying constraints.

For more information, check [here](https://charticulator.com/).

## Load data

It is possible to link or browse the data from the local PC.

## Import a charticulator template

Clicking the  icon in the toolbar will display a file open dialog so that one can select a template file from the local folders.

## Save to My Charts

Chart designs can be saved to the _My Charts_ list. Please note that the data and charts remain local in the user browser unless downloaded as a chart file.

``` {note}
It is possible to transfer and syncronize local files and directories (including the new generated charts)
with UCloud through [Rsync Server](rsync.md) and [MinIO](minio.md) Apps.
```
