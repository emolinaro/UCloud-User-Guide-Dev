# FEniCSx

:::: {tab-set}

::: {tab-item} 0.7.2

[![](badges/release-0.7.2-blue.svg)](https://cloud.sdu.dk/app/jobs/create?app=fenicsx&version=0.7.2)
![type](badges/type-interactive-yellow.svg)
![access](badges/access-open-green.svg)
* **Operating System:** ![](./badges/Ubuntu-22.04-lightseagreen.svg)
* **Terminal:** ![](./badges/tini-0.19.0-lightseagreen.svg) ![](./badges/tmux-3.2a-lightseagreen.svg)
* **Shell:** ![](./badges/bash-5.1.16-lightseagreen.svg) ![](./badges/fish-3.3.1-lightseagreen.svg) ![](./badges/zsh-5.8.1-lightseagreen.svg)
* **Editor:** ![](./badges/emacs-27.1-lightseagreen.svg) ![](./badges/nano-6.2-lightseagreen.svg) ![](./badges/vim-8.2-lightseagreen.svg)
* **Package Manager:** ![](./badges/apt-2.4.10-lightseagreen.svg) ![](./badges/dpkg-1.21.1-lightseagreen.svg) ![](./badges/pip-23.2.1-lightseagreen.svg)
* **Programming Language:** ![](./badges/GCC-11.4.0-lightseagreen.svg) ![](./badges/Python-3.10.12-lightseagreen.svg)
* **Extension:** ![](./badges/OpenMPI-4.1.2-lightseagreen.svg)

:::

::: {tab-item} 0.6.0

[![](badges/release-0.6.0-blue.svg)](https://cloud.sdu.dk/app/jobs/create?app=fenicsx&version=0.6.0)
![type](badges/type-interactive-yellow.svg)
![access](badges/access-open-green.svg)
* **Operating System:** ![](./badges/Ubuntu-22.04-lightseagreen.svg)
* **Terminal:** ![](./badges/tini-0.19.0-lightseagreen.svg) ![](./badges/tmux-3.2a-lightseagreen.svg)
* **Shell:** ![](./badges/bash-5.1.16-lightseagreen.svg)
* **Editor:** ![](./badges/emacs-27.1-lightseagreen.svg) ![](./badges/nano-6.2-lightseagreen.svg) ![](./badges/vim-8.2-lightseagreen.svg)
* **Package Manager:** ![](./badges/apt-2.4.8-lightseagreen.svg) ![](./badges/dpkg-1.21.1-lightseagreen.svg) ![](./badges/pip-22.0.2-lightseagreen.svg)
* **Programming Language:** ![](./badges/GCC-11.3.0-lightseagreen.svg) ![](./badges/Python-3.10.6-lightseagreen.svg)
* **Extension:** ![](./badges/OpenMPI-4.0.3-lightseagreen.svg)

:::

::: {tab-item} 0.5.1

[![](badges/release-0.5.1-blue.svg)](https://cloud.sdu.dk/app/jobs/create?app=fenicsx&version=0.5.1)
![type](badges/type-interactive-yellow.svg)
![access](badges/access-open-green.svg)
* **Operating System:** ![](./badges/Ubuntu-22.04-lightseagreen.svg)
* **Terminal:** ![](./badges/tmux-3.2a-lightseagreen.svg)
* **Shell:** ![](./badges/bash-5.1.16-lightseagreen.svg)
* **Editor:** ![](./badges/emacs-27.1-lightseagreen.svg) ![](./badges/nano-6.2-lightseagreen.svg) ![](./badges/vim-8.2-lightseagreen.svg)
* **Package Manager:** ![](./badges/apt-2.4.8-lightseagreen.svg) ![](./badges/dpkg-1.21.1-lightseagreen.svg) ![](./badges/pip-22.0.2-lightseagreen.svg)
* **Programming Language:** ![](./badges/GCC-11.3.0-lightseagreen.svg) ![](./badges/Python-3.10.6-lightseagreen.svg)

:::

::: {tab-item} 0.4.1

[![](badges/release-0.4.1-blue.svg)](https://cloud.sdu.dk/app/jobs/create?app=fenicsx&version=0.4.1)
![type](badges/type-interactive-yellow.svg)
![access](badges/access-open-green.svg)
* **Operating System:** ![](./badges/Ubuntu-21.10-lightseagreen.svg)
* **Terminal:** ![](./badges/tmux-3.1c-lightseagreen.svg)
* **Shell:** ![](./badges/bash-5.1.8-lightseagreen.svg)
* **Editor:** ![](./badges/emacs-27.1-lightseagreen.svg) ![](./badges/nano-5.6.1-lightseagreen.svg) ![](./badges/vim-8.2-lightseagreen.svg)
* **Package Manager:** ![](./badges/apt-2.3.9-lightseagreen.svg) ![](./badges/dpkg-1.20.9-lightseagreen.svg) ![](./badges/pip-20.3.4-lightseagreen.svg)
* **Programming Language:** ![](./badges/GCC-11.2.0-lightseagreen.svg) ![](./badges/Python-3.9.7-lightseagreen.svg)

:::

::::

The FEniCSx Project is a collection of free and open-source software components with the common goal of enabling automated solution of differential equations.
The components provide scientific computing tools for working with computational meshes, finite-element variational formulations of ordinary and partial differential equations, and numerical linear algebra with the high-level Python and C++ interfaces.

For more information, check [here](https://fenicsproject.org/).

## Select input parameters

FEniCSx can be run either in batch mode or interactively.
When the *Interactive mode* option is selected, a Jupyter Notebook interface is accessible.

If FEniCSx is executed in batch mode then the following two input parameters must be specified:

- *Input file*: the main source file for the app, namely a script.py file. (Requires to mount the folder which contains the script).

- *Mount* data folder: the directory with the data and the source code. This parameter is optional while running in interactive mode.

Additional packages can be installed inside the application container using the *Initialization* parameter.
The user should provide the list of packages via a text file (`.txt`).
The installation is done via the `pip3` package installer.
