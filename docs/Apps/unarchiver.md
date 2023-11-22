# Unarchiver

:::: {tab-set}

::: {tab-item} 0.2.0

[![Unarchiver v0.2.0](badges/release-0.2.0-blue.svg)](https://cloud.sdu.dk/app/jobs/create?app=unarchiver&version=0.2.0)
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

::: {tab-item} 0.1.2

[![Unarchiver v0.1.2](badges/release-0.1.2-blue.svg)](https://cloud.sdu.dk/app/jobs/create?app=unarchiver&version=0.1.2)
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

This utility is used to submit a batch job that extracts files from a compressed archive. The latter should be selected using the *Archive file* parameter.
The contents of the archive are available in the `extracted_files` folder.

## Supported archive files

| **Archive Format**               | **File Extension**                      |
|----------------------------------|-----------------------------------------|
| 7-Zip Compressed File            | ``.7z`` \, ``.tar.7z``                  |
| BZip Compressed File             | ``.bz`` \, ``.tar.bz`` \, ``.tbz``      |
| Bzip2 Compressed File            | ``.bz2`` \, ``.tar.bz2`` \, ``.tbz2``   |
| Debian Software Package          | ``.deb``                                |
| Apple Disk Image                 | ``.dmg``                                |
| GNU Zipped File                  | ``.gz`` \, ``.tar.gz`` \, ``.tgz``      |
| HFS Disk Image File              | ``.hfs``                                |
| ISO Disk Image File              | ``.iso``                                |
| LZMA Compressed File             | ``.lzma`` \, ``.tar.lzma`` \, ``.tlz``  |
| NTFS Partition File              | ``.ntfs``                               |
| WinRAR Compressed File           | ``.rar``                                |
| Red Hat Package Manager File     | ``.rpm``                                |
| GNU Tarball File                 | ``.tar``                                |
| Universal Disk Format File       | ``.udf``                                |
| Virtual Hard Disk File           | ``.vhd``                                |
| Windows Imaging Format File      | ``.wim``                                |
| XZ Compressed File               | ``.xz`` \, ``.tar.xz`` \, ``.txz``      |
| Unix Compressed File             | ``.z``                                  |
| Zipped File                      | ``.zip``                                |
