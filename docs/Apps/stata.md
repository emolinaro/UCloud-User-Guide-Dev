# Stata

:::: {tab-set}

::: {tab-item} 18

[![](badges/release-18-blue.svg)](https://cloud.sdu.dk/app/jobs/create?app=stata&version=18)
![type](badges/type-VDE-yellow.svg)
![access](badges/access-restricted-red.svg)
* **Operating System:** ![](./badges/Ubuntu-22.04-lightseagreen.svg)
* **Terminal:** ![](./badges/tini-0.19.0-lightseagreen.svg) ![](./badges/tmux-3.2a-lightseagreen.svg)
* **Shell:** ![](./badges/bash-5.1.16-lightseagreen.svg) ![](./badges/fish-3.3.1-lightseagreen.svg) ![](./badges/zsh-5.8.1-lightseagreen.svg)
* **Editor:** ![](./badges/emacs-27.1-lightseagreen.svg) ![](./badges/nano-6.2-lightseagreen.svg) ![](./badges/vim-8.2-lightseagreen.svg)
* **Package Manager:** ![](./badges/apt-2.4.10-lightseagreen.svg) ![](./badges/dpkg-1.21.1-lightseagreen.svg) ![](./badges/npm-8.5.1-lightseagreen.svg) ![](./badges/pip-23.2.1-lightseagreen.svg)
* **Programming Language:** ![](./badges/GCC-11.4.0-lightseagreen.svg) ![](./badges/Mono-6.8.0.105-lightseagreen.svg) ![](./badges/OpenJDK-11.0.20.1-lightseagreen.svg) ![](./badges/Python-3.10.12-lightseagreen.svg)
* **Database:** ![](./badges/SQLite-3.37.2-lightseagreen.svg)

:::

::: {tab-item} 17

[![](badges/release-17-blue.svg)](https://cloud.sdu.dk/app/jobs/create?app=stata&version=17)
![type](badges/type-VDE-yellow.svg)
![access](badges/access-restricted-red.svg)
* **Operating System:** ![](./badges/Ubuntu-20.04-lightseagreen.svg)
* **Terminal:** ![](./badges/tmux-3.0a-lightseagreen.svg)
* **Shell:** ![](./badges/bash-5.0.17-lightseagreen.svg)
* **Editor:** ![](./badges/emacs-26.3-lightseagreen.svg) ![](./badges/nano-4.8-lightseagreen.svg) ![](./badges/vim-8.1-lightseagreen.svg)
* **Package Manager:** ![](./badges/apt-2.0.6-lightseagreen.svg) ![](./badges/dpkg-1.19.7-lightseagreen.svg) ![](./badges/pip-21.3-lightseagreen.svg)
* **Programming Language:** ![](./badges/GCC-9.3.0-lightseagreen.svg) ![](./badges/OpenJDK-11.0.11-lightseagreen.svg) ![](./badges/Python-3.8.10-lightseagreen.svg)
* **Database:** ![](./badges/SQLite-3.31.1-lightseagreen.svg)

:::

::: {tab-item} 16

[![](badges/release-16-blue.svg)](https://cloud.sdu.dk/app/jobs/create?app=stata&version=16-1)
![type](badges/type-VDE-yellow.svg)
![access](badges/access-restricted-red.svg)
* **Operating System:** ![](./badges/Ubuntu-18.04-lightseagreen.svg)
* **Shell:** ![](./badges/bash-4.4.20-lightseagreen.svg)
* **Editor:** ![](./badges/emacs-25.2.2-lightseagreen.svg) ![](./badges/nano-2.9.3-lightseagreen.svg) ![](./badges/vim-8.0-lightseagreen.svg)
* **Package Manager:** ![](./badges/apt-1.6.12-lightseagreen.svg) ![](./badges/dpkg-1.19.0.5-lightseagreen.svg) ![](./badges/pip-20.0.2-lightseagreen.svg)
* **Programming Language:** ![](./badges/GCC-7.4.0-lightseagreen.svg) ![](./badges/OpenJDK-1.8.0-lightseagreen.svg) ![](./badges/Python-3.6.9-lightseagreen.svg) ![](./badges/Python-2.7.17-lightseagreen.svg)
* **Database:** ![](./badges/SQLite-3.22.0-lightseagreen.svg)

:::

::::

Stata is a general-purpose statistical software for data science that enables users to analyze, manage, and produce graphical visualizations of data. It is primarily used by researchers in the fields of economics, biomedicine, and political science to examine data patterns.

For more information, check [here](https://www.stata.com/features/documentation/).

## Import a single-user license

The parameter *Stata license* must be used to import a Stata single-user license file.

Alternatively, the user can activate a new license using the *Terminal* window of the virtual desktop:

```console
$ cd $STATA_HOME
$ sudo ./stinit
```

In this case, the user must provide the license's *serial number*, *code* and *authorization* keys.

## Connect to a network license

Depending on the user institution, it is also possible to request access to a Stata network license server using the parameter *Select Stata license server*.
Network licenses must be added to an active project by means of a [grant application](../guide/resources-grant.md). Project admins can restrict access to the license as discussed [here](../guide/project-overview.md).
