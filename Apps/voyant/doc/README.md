# Voyant Server

:::: {tab-set}

::: {tab-item} 2.6.10

[![](badges/release-2.6.10-blue.svg)](https://cloud.sdu.dk/app/jobs/create?app=voyantserver&version=2.6.10)
[![type](badges/type-interactive-yellow.svg)](interactive_apps.md)
![access](badges/access-open-green.svg)
* **Operating System:** ![](./badges/Ubuntu-22.04-lightseagreen.svg)
* **Terminal:** ![](./badges/tini-0.19.0-lightseagreen.svg) ![](./badges/tmux-3.2a-lightseagreen.svg)
* **Shell:** ![](./badges/bash-5.1.16-lightseagreen.svg) ![](./badges/fish-3.3.1-lightseagreen.svg) ![](./badges/zsh-5.8.1-lightseagreen.svg)
* **Editor:** ![](./badges/emacs-27.1-lightseagreen.svg) ![](./badges/nano-6.2-lightseagreen.svg) ![](./badges/vim-8.2-lightseagreen.svg)
* **Package Manager:** ![](./badges/apt-2.4.10-lightseagreen.svg) ![](./badges/dpkg-1.21.1-lightseagreen.svg) ![](./badges/npm-8.5.1-lightseagreen.svg) ![](./badges/pip-22.0.2-lightseagreen.svg)
* **Programming Language:** ![](./badges/GCC-11.4.0-lightseagreen.svg) ![](./badges/OpenJDK-11.0.20.1-lightseagreen.svg) ![](./badges/Python-3.10.12-lightseagreen.svg)
* **Utility:** ![](./badges/EasyBuild-4.8.1-lightseagreen.svg) ![](./badges/Lmod-8.7-lightseagreen.svg)
* **Extension:** ![](./badges/OpenMPI-4.1.2-lightseagreen.svg)

:::

::: {tab-item} 2.5.3

[![](badges/release-2.5.3-blue.svg)](https://cloud.sdu.dk/app/jobs/create?app=voyantserver&version=2.5.3)
[![type](badges/type-interactive-yellow.svg)](interactive_apps.md)
![access](badges/access-open-green.svg)
* **Operating System:** ![](./badges/Ubuntu-20.04-lightseagreen.svg)
* **Terminal:** ![](./badges/tmux-3.0a-lightseagreen.svg)
* **Shell:** ![](./badges/bash-5.0.17-lightseagreen.svg)
* **Editor:** ![](./badges/emacs-26.3-lightseagreen.svg) ![](./badges/nano-4.8-lightseagreen.svg) ![](./badges/vim-8.1-lightseagreen.svg)
* **Package Manager:** ![](./badges/apt-2.0.6-lightseagreen.svg) ![](./badges/dpkg-1.19.7-lightseagreen.svg)
* **Programming Language:** ![](./badges/OpenJDK-1.8.0-lightseagreen.svg)

:::

::::

Voyant Server is a standalone version of the Voyant Tools server, i.e. a web-based text reading and analysis environment. It is a scholarly project that is designed to facilitate reading and interpretive practices for digital humanities students and scholars as well as for the general public.

For more information, check [here](https://voyant-tools.org/docs/#!/guide)

## Select the data folder

By default the data folder is a temporary directory.

However, through the option *DATA_DIR* it is possible to specify the path to an existing directory.

``` {note}
In this case the default example data (currently the Shakespeare, Austen's Novels and Mary Shelley's Frankenstein corpora) are not accessible, if not present in your data folder.
```

If the folder selected with the *DATA_DIR* option is empty, the default example directory can be included with the option *-e*.

## Add corpora to the drop down menu

The option *-c* (used in combination with *DATA_DIR*) defines which corpora appear in the drop-down menu.
If this option is not selected then the default value is used (currently the Austen and Shakespeare corpora).

Corpora are defined using a special syntax and multiple corpora are separated by semi-colon. For instance, by writing the string:

```console
mycorpora1:title1;mycorpora2:title2
```

*mycorpora1* and *mycorpora2* correspond to the folder names in the `trombone5_2/corpora` subdirectory of the *DATA_DIR* path, while *title1* and *title2* correspond to the menu items.

## Access a Spyral Notebook

A *Spyral Notebook* is accessible by adding `/spyral` to the web page URL.

Spyral Notebooks are dynamic documents that combine writing, code and data in service of reading, analyzing and interpreting digital texts.
