# Intertext

[![](badges/release-0.1.0-blue.svg)](https://cloud.sdu.dk/app/jobs/create?app=intertext&version=0.1.0-5)
[![type](badges/type-interactive-yellow.svg)](interactive_apps.md)
![access](badges/access-open-green.svg)
* **Operating System:** ![](./badges/Debian-10-lightseagreen.svg)
* **Shell:** ![](./badges/bash-5.0.3-lightseagreen.svg)
* **Editor:** ![](./badges/vim-8.1-lightseagreen.svg)
* **Package Manager:** ![](./badges/apt-1.8.2.1-lightseagreen.svg) ![](./badges/conda-4.9.2-lightseagreen.svg) ![](./badges/dpkg-1.19.7-lightseagreen.svg) ![](./badges/npm-6.4.1-lightseagreen.svg) ![](./badges/pip-21.0.1-lightseagreen.svg)
* **Programming Language:** ![](./badges/GCC-8.3.0-lightseagreen.svg) ![](./badges/Python-3.6.13-lightseagreen.svg) ![](./badges/Python-2.7.16-lightseagreen.svg)
* **Database:** ![](./badges/SQLite-3.35.4-lightseagreen.svg)
---

Intertext combines machine learning with interactive data visualizations to surface intertextual patterns in large text collections. The text processing is based on min-hashing vectorized strings, and the web viewer is based on interactive React components.

For more information, check [here](https://github.com/YaleDHLab/intertext).

## Input database folder

The app receives a mandatory parameter, *database dir*, namely the directory in which the app backend MongoDB database will store data. By selecting the database directory it is possible to detect reuse in the included sample documents and visualize the results by starting the job.

## Using custom text files

To discover text reuse in your own text files, it is necessary to select the optional parameters *infiles* and *metadata* and specify the directory with your text files and the metadata directory which contains the metadata file. The new text files and the metadata files have to be in the same format as the sample files (see https://github.com/YaleDHLab/intertext).

Additional optional parameters allow to control the way Intertext discovers text reuse in a text corpus.

Additional packages can be installed inside the application container using the *Additional dependencies* parameter,
by loading a Bash script (`*.sh`) with the list of shell commands to be used for the installation.

## Configure custom public links

In order to share a public link of the running app with non-registered users it is necessary to deploy the app with a [public URL](general_settings.md#configure-custom-links).
In addition it is important to select the option *Enable public link* and write exactly the same string used to identify the public link in the *Configure custom links* field, e.g.:
<br>

<img src="figs/intertext-enablepl.png" alt="drawing" width="80%" align="center">

<br>
and
<br>

<img src="figs/intertext-pl.png" alt="drawing" width="80%" align="center">
