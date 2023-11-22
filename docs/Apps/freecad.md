# FreeCAD

:::: {tab-set}

::: {tab-item} 0.20.1

[![freecad](badges/release-0.20.1-blue.svg)](https://cloud.sdu.dk/app/jobs/create?app=freecad&version=0.20.1)
![type](badges/type-VDE-yellow.svg)
![access](badges/access-open-green.svg)
* **Operating System:** ![](./badges/Ubuntu-22.04-lightseagreen.svg)
* **Terminal:** ![](./badges/tini-0.19.0-lightseagreen.svg) ![](./badges/tmux-3.2a-lightseagreen.svg)
* **Shell:** ![](./badges/bash-5.1.16-lightseagreen.svg) ![](./badges/fish-3.3.1-lightseagreen.svg) ![](./badges/zsh-5.8.1-lightseagreen.svg)
* **Editor:** ![](./badges/emacs-27.1-lightseagreen.svg) ![](./badges/nano-6.2-lightseagreen.svg) ![](./badges/vim-8.2-lightseagreen.svg)
* **Package Manager:** ![](./badges/apt-2.4.10-lightseagreen.svg) ![](./badges/dpkg-1.21.1-lightseagreen.svg) ![](./badges/npm-8.5.1-lightseagreen.svg) ![](./badges/pip-23.2.1-lightseagreen.svg)
* **Programming Language:** ![](./badges/GCC-11.4.0-lightseagreen.svg) ![](./badges/Mono-6.8.0.105-lightseagreen.svg) ![](./badges/OpenJDK-11.0.20.1-lightseagreen.svg) ![](./badges/Python-3.10.12-lightseagreen.svg)
* **Database:** ![](./badges/SQLite-3.37.2-lightseagreen.svg)
* **Utility:** ![](./badges/EasyBuild-4.8.1-lightseagreen.svg) ![](./badges/Lmod-8.7-lightseagreen.svg)
* **Extension:** ![](./badges/OpenMPI-4.1.2-lightseagreen.svg)

:::

::: {tab-item} 0.18.4

[![freecad](badges/release-0.18.4-blue.svg)](https://cloud.sdu.dk/app/jobs/create?app=freecad&version=0.18.4-1)
![type](badges/type-VDE-yellow.svg)
![access](badges/access-open-green.svg)
* **Operating System:** ![](./badges/Ubuntu-18.04-lightseagreen.svg)
* **Shell:** ![](./badges/bash-4.4.20-lightseagreen.svg)
* **Editor:** ![](./badges/emacs-25.2.2-lightseagreen.svg) ![](./badges/nano-2.9.3-lightseagreen.svg) ![](./badges/vim-8.0-lightseagreen.svg)
* **Package Manager:** ![](./badges/apt-1.6.11-lightseagreen.svg) ![](./badges/dpkg-1.19.0.5-lightseagreen.svg) ![](./badges/pip-20.0.2-lightseagreen.svg)
* **Programming Language:** ![](./badges/GCC-7.4.0-lightseagreen.svg) ![](./badges/OpenJDK-1.8.0-lightseagreen.svg) ![](./badges/Python-3.6.9-lightseagreen.svg) ![](./badges/Python-2.7.17-lightseagreen.svg)
* **Database:** ![](./badges/SQLite-3.22.0-lightseagreen.svg)
:::

::::

FreeCAD is a general-purpose parametric 3D computer-aided design (CAD) modeler and a building information modeling (BIM) software with finite element method (FEM) support. FreeCAD is intended for mechanical engineering product design but also expands to architecture or electrical engineering. Users can extend the functionality of the software using the Python programming language. Meshing tools include Gmsh and Netgen (netgen-mesher).

For more information, check [here](https://www.freecadweb.org).

## Getting started

FreeCAD, Gmsh and Netgen can be started by double-clicking on the corresponding desktop icons. They can also be started directly from the command line by typing `freecad`, `gmsh` or `netgen`, respectively. This allows to change some of the default startup options.

Current options are available by typing:

```console
$ freecad --help
```

## Running without GUI

FreeCAD can be used in console mode using the `-c` switch from the command line:

```console
$ freecad -c
```

or by using the command:

```console
$ freecadcmd
```

In console mode, no user interface will be displayed, and you will be presented with a Python interpreter prompt.
