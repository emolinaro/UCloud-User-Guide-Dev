# SIESTA

[![SIESTA](badges/release-4.1-b3-blue.svg)](https://cloud.sdu.dk/app/jobs/create?app=siesta&version=4.1-b3-1)
![type](badges/type-VDE-yellow.svg)
![access](badges/access-open-green.svg)
* **Operating System:** ![](./badges/Ubuntu-18.04-lightseagreen.svg)
* **Shell:** ![](./badges/bash-4.4.20-lightseagreen.svg)
* **Editor:** ![](./badges/emacs-25.2.2-lightseagreen.svg) ![](./badges/nano-2.9.3-lightseagreen.svg) ![](./badges/vim-8.0-lightseagreen.svg)
* **Package Manager:** ![](./badges/apt-1.6.11-lightseagreen.svg) ![](./badges/dpkg-1.19.0.5-lightseagreen.svg) ![](./badges/pip-20.0.2-lightseagreen.svg)
* **Programming Language:** ![](./badges/GCC-7.5.0-lightseagreen.svg) ![](./badges/OpenJDK-1.8.0-lightseagreen.svg) ![](./badges/Python-3.6.9-lightseagreen.svg) ![](./badges/Python-2.7.17-lightseagreen.svg)
* **Database:** ![](./badges/SQLite-3.22.0-lightseagreen.svg)
---

SIESTA is a density-functional theory code which allows to perform efficient electronic structure calculations and ab initio molecular dynamics simulations of molecules and solids with the use of a basis set of strictly-localized atomic orbitals.

More informations can be found [here](https://departments.icmab.es/leem/siesta/Documentation/index.md).

## Getting Started

Open the terminal and access your project directory in `/work`, where you have the required files, namely the input file and a pseudopotential file (`.vps` or `.psf`) for every atomic species included in the input file.

Run the code:

```console
$ siesta < file.fdf > file.out
```

or to run in parallel:

```console
$ mpirun -np <number> siesta < file.fdf > file.out
```

Example `.fdf` and pseudopotential files can be found in `$SIESTA_DIR/siesta-4.1-b3/Examples` and ready-to-run examples in `$SIESTA_DIR/siesta-4.1-b3/Tests`.
