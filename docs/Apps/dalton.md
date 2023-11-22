# Dalton

:::: {tab-set}

::: {tab-item} 2020.1

[![Dalton 2020.1](badges/release-2020.1-blue.svg)](https://cloud.sdu.dk/app/jobs/create?app=dalton&version=2020.1)
![type](badges/type-batch-yellow.svg)
![access](badges/access-open-green.svg)
* **Operating System:** ![](./badges/Ubuntu-22.04-lightseagreen.svg)
* **Terminal:** ![](./badges/tini-0.19.0-lightseagreen.svg) ![](./badges/tmux-3.2a-lightseagreen.svg)
* **Shell:** ![](./badges/bash-5.1.16-lightseagreen.svg) ![](./badges/fish-3.3.1-lightseagreen.svg) ![](./badges/zsh-5.8.1-lightseagreen.svg)
* **Editor:** ![](./badges/emacs-27.1-lightseagreen.svg) ![](./badges/nano-6.2-lightseagreen.svg) ![](./badges/vim-8.2-lightseagreen.svg)
* **Package Manager:** ![](./badges/apt-2.4.10-lightseagreen.svg) ![](./badges/dpkg-1.21.1-lightseagreen.svg) ![](./badges/npm-8.5.1-lightseagreen.svg) ![](./badges/pip-22.0.2-lightseagreen.svg)
* **Programming Language:** ![](./badges/GCC-11.4.0-lightseagreen.svg) ![](./badges/Python-3.10.12-lightseagreen.svg)
* **Utility:** ![](./badges/EasyBuild-4.8.1-lightseagreen.svg) ![](./badges/Lmod-8.7-lightseagreen.svg)
* **Extension:** ![](./badges/OpenMPI-4.1.2-lightseagreen.svg)

:::

::: {tab-item} 2020.0

[![Dalton 2020.0](badges/release-2020.0-blue.svg)](https://cloud.sdu.dk/app/jobs/create?app=dalton&version=2020.0)
![type](badges/type-batch-yellow.svg)
![access](badges/access-open-green.svg)
* **Operating System:** ![](./badges/Ubuntu-20.04-lightseagreen.svg)
* **Shell:** ![](./badges/bash-5.0.17-lightseagreen.svg)
* **Editor:** ![](./badges/emacs-26.3-lightseagreen.svg) ![](./badges/nano-4.8-lightseagreen.svg) ![](./badges/vim-8.1-lightseagreen.svg)
* **Package Manager:** ![](./badges/apt-2.0.6-lightseagreen.svg) ![](./badges/dpkg-1.19.7-lightseagreen.svg)
* **Programming Language:** ![](./badges/GCC-9.3.0-lightseagreen.svg) ![](./badges/Python-3.8.10-lightseagreen.svg)

:::

::::

The Dalton program is designed to allow convenient, automated determination of a large number of molecular properties based on an HF, HF-srDFT, DFT, MP2, CC, CI, MCSCF, or MC-srDFT reference wave function.

Homepage for the Dalton program can be found at [daltonprogram.org](https://daltonprogram.org/).
Documentation for the Dalton program can be found [here](https://daltonprogram.org/manuals/dalton2020manual.pdf).

## Batch mode (default)

The app receives the following two *mandatory* parameters:

- *molecule file*: File containing molecular coordinates, molecular charge, and basis-set specifications.
- *dalton input file*: File containing information about electronic-structure methods to be used.

## Interactive mode

By selecting the _interactive mode_, the user can open a terminal window
available on the progress view page of the job and run Dalton from the command line.
All *optional* parameters given through the UCloud interface will be ignored when starting _interactive mode_.
Dalton can be run from the command line by calling `dalton`, e.g.:

```console
dalton -np 4 -dal <filename>.dal -mol <filename>.mol
```

More options can be given when calling the Dalton program from the command line.
See the [Dalton documentation](https://daltonprogram.org/manuals/dalton2020manual.pdf) for additional options.
