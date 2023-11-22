# Salmon

:::: {tab-set}

::: {tab-item} 1.10.2

[![](badges/release-1.10.2-blue.svg)](https://cloud.sdu.dk/app/search/applications?query=salmon)
![type](badges/type-batch-yellow.svg)
![access](badges/access-open-green.svg)
* **Operating System:** ![](./badges/Ubuntu-22.10-lightseagreen.svg)
* **Terminal:** ![](./badges/tini-0.19.0-lightseagreen.svg) ![](./badges/tmux-3.3a-lightseagreen.svg)
* **Shell:** ![](./badges/bash-5.2.2-lightseagreen.svg) ![](./badges/fish-3.5.1-lightseagreen.svg) ![](./badges/zsh-5.9-lightseagreen.svg)
* **Editor:** ![](./badges/emacs-27.1-lightseagreen.svg) ![](./badges/nano-6.4-lightseagreen.svg) ![](./badges/vim-9.0-lightseagreen.svg)
* **Package Manager:** ![](./badges/apt-2.5.3-lightseagreen.svg) ![](./badges/conda-23.1.0-lightseagreen.svg) ![](./badges/dpkg-1.21.9-lightseagreen.svg) ![](./badges/npm-8.18.0-lightseagreen.svg) ![](./badges/pip-23.1.2-lightseagreen.svg)
* **Programming Language:** ![](./badges/GCC-12.2.0-lightseagreen.svg) ![](./badges/OpenJDK-11.0.19-lightseagreen.svg) ![](./badges/Python-3.10.12-lightseagreen.svg) ![](./badges/Python-2.7.18-lightseagreen.svg)
* **Utility:** ![](./badges/Lmod-8.7-lightseagreen.svg)
* **Extension:** ![](./badges/OpenMPI-4.1.4-lightseagreen.svg)

:::

::: {tab-item} 1.3.0

[![](badges/release-1.3.0-blue.svg)](https://cloud.sdu.dk/app/search/applications?query=salmon)
![type](badges/type-batch-yellow.svg)
![access](badges/access-open-green.svg)
* **Operating System:** ![](./badges/Debian-10.3-lightseagreen.svg)
* **Shell:** ![](./badges/bash-5.0.3-lightseagreen.svg)
* **Editor:** ![](./badges/vim-8.1-lightseagreen.svg)
* **Package Manager:** ![](./badges/apt-1.8.2-lightseagreen.svg) ![](./badges/conda-4.9.2-lightseagreen.svg) ![](./badges/dpkg-1.19.7-lightseagreen.svg)
* **Programming Language:** ![](./badges/GCC-8.3.0-lightseagreen.svg) ![](./badges/Python-3.7.6-lightseagreen.svg) ![](./badges/Python-2.7.16-lightseagreen.svg)
* **Database:** ![](./badges/SQLite-3.33.0-lightseagreen.svg)

:::

::: {tab-item} 0.12.0

[![](badges/release-0.12.0-blue.svg)](https://cloud.sdu.dk/app/search/applications?query=salmon)
![type](badges/type-batch-yellow.svg)
![access](badges/access-open-green.svg)

* **Operating System:** ![](./badges/Debian-10.1-lightseagreen.svg)
* **Shell:** ![](./badges/bash-5.0.3-lightseagreen.svg)
* **Editor:** ![](./badges/vim-8.1-lightseagreen.svg)
* **Package Manager:** ![](./badges/apt-1.8.2-lightseagreen.svg) ![](./badges/conda-4.8.2-lightseagreen.svg) ![](./badges/dpkg-1.19.7-lightseagreen.svg) ![](./badges/pip-20.0.2-lightseagreen.svg)
* **Programming Language:** ![](./badges/GCC-8.3.0-lightseagreen.svg) ![](./badges/Python-3.7.4-lightseagreen.svg) ![](./badges/Python-2.7.16-lightseagreen.svg)
* **Database:** ![](./badges/SQLite-3.31.1-lightseagreen.svg)

:::

::::

Salmon is a wicked-fast program to produce a highly-accurate, transcript-level
quantification estimates from RNA-seq data. Salmon achieves its accuracy and speed
via a number of different innovations, including the use of quasi-mapping (accurate
but fast-to-compute proxies for traditional read alignments), and massively-parallel
stochastic collapsed variational inference. The result is a versatile tool that
fits nicely into many different pipelines.

For more information, check [here](https://salmon.readthedocs.io/en/latest/).

<details>
  <summary>Salmon utilities</summary>

- [![alevin](badges/alevin-yellowgreen.svg)](https://cloud.sdu.dk/app/jobs/create?app=salmon-alevin&version=1.10.2)
- [![index](badges/index-yellowgreen.svg)](https://cloud.sdu.dk/app/jobs/create?app=salmon-index&version=1.10.2)
- [![quant alignment](badges/quant-alignment-yellowgreen.svg)](https://cloud.sdu.dk/app/jobs/create?app=salmon-quant-alignment&version=1.10.2)
- [![quant merge](badges/quant-merge-yellowgreen.svg)](https://cloud.sdu.dk/app/jobs/create?app=salmon-quantmerge&version=1.10.2)
- [![quant reads](badges/quant-reads-yellowgreen.svg)](https://cloud.sdu.dk/app/jobs/create?app=salmon-quant-reads&version=1.10.2)
</details>
