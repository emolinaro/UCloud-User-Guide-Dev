# CentOS Xfce

:::: {tab-set}

::: {tab-item} CentOS 8.5

[![CentOS Xfce v8](badges/release-8.5-blue.svg)](https://cloud.sdu.dk/app/jobs/create?app=centos-xfce&version=8.5)
![type](badges/type-VDE-yellow.svg)
![access](badges/access-open-green.svg)
* **Operating System:** ![](./badges/CentOS-8.5-lightseagreen.svg)
* **Terminal:** ![](./badges/tmux-2.7-lightseagreen.svg)
* **Shell:** ![](./badges/bash-4.4.20-lightseagreen.svg)
* **Editor:** ![](./badges/emacs-26.1-lightseagreen.svg) ![](./badges/vim-8.0-lightseagreen.svg)
* **Package Manager:** ![](./badges/dnf-4.7.0-lightseagreen.svg) ![](./badges/pip-21.3.1-lightseagreen.svg) ![](./badges/rpm-4.14.3-lightseagreen.svg) ![](./badges/yum-4.7.0-lightseagreen.svg)
* **Programming Language:** ![](./badges/GCC-8.5.0-lightseagreen.svg) ![](./badges/OpenJDK-11.0.13-lightseagreen.svg) ![](./badges/Python-3.6.8-lightseagreen.svg)
* **Utility:** ![](./badges/EasyBuild-4.5.4-lightseagreen.svg) ![](./badges/Lmod-8.6-lightseagreen.svg)

:::

::: {tab-item} CentOS 7.9

[![CentOS Xfce v7](badges/release-7-blue.svg)](https://cloud.sdu.dk/app/jobs/create?app=centos-xfce&version=7)
![type](badges/type-VDE-yellow.svg)
![access](badges/access-open-green.svg)
* **Operating System:** ![](./badges/CentOS-7.9-lightseagreen.svg)
* **Shell:** ![](./badges/bash-4.2.46-lightseagreen.svg)
* **Editor:** ![](./badges/emacs-24.3.1-lightseagreen.svg) ![](./badges/nano-2.3.1-lightseagreen.svg) ![](./badges/vim-7.4-lightseagreen.svg)
* **Package Manager:** ![](./badges/pip-20.0.2-lightseagreen.svg) ![](./badges/rpm-4.11.3-lightseagreen.svg) ![](./badges/yum-3.4.3-lightseagreen.svg)
* **Programming Language:** ![](./badges/OpenJDK-1.8.0-lightseagreen.svg) ![](./badges/Python-3.6.8-lightseagreen.svg) ![](./badges/Python-2.7.5-lightseagreen.svg)
* **Database:** ![](./badges/SQLite-3.7.17-lightseagreen.svg)

:::

::::

Interactive CentOS virtual desktop environment, terminal and browsers.

## Initialization

For information on how to use the *Initialization* parameter, please refer to the [Initialization - Bash script](../hands-on/init-sh.md) section of the documentation.

## Additional software

New software applications can be installed and accessed as separate modules using EasyBuild, a build and installation framework for the deployment and management of scientific applications/tools on HPC systems.
A brief introduction to EasyBuild is available [here](terminal.md#easybuild).

New software modules should be installed in a directory accessible from the _default working tree_, e.g. `/work/sandbox`. As a result, the `sandbox` software stack will be available in the UCloud workspace once the job is completed. The user should mount this folder as a data volume inside the app and make the new modules available from the command-line interface:

```console
$ module use /work/sandbox/modules/all/
```

To check all available modules, use the command:

```console
$ module avail
```

More commands are listed [here](terminal.md#environment-modules).

``` {note}
Environment modules are loaded automatically when the ``sandbox`` folder is mounted using the optional *Modules path* parameter.
```
