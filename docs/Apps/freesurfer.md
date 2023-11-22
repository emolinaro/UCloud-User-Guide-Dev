# FreeSurfer

:::: {tab-set}

::: {tab-item} 7.4.1

[![](badges/release-7.4.1-blue.svg)](https://cloud.sdu.dk/app/jobs/create?app=freesurfer&version=7.4.1)
![type](badges/type-VDE-yellow.svg)
![access](badges/access-restricted-red.svg)
* **Operating System:** ![](./badges/Ubuntu-20.04-lightseagreen.svg)
* **Terminal:** ![](./badges/tini-0.19.0-lightseagreen.svg) ![](./badges/tmux-3.0a-lightseagreen.svg)
* **Shell:** ![](./badges/bash-5.0.17-lightseagreen.svg) ![](./badges/fish-3.1.0-lightseagreen.svg) ![](./badges/zsh-5.8-lightseagreen.svg)
* **Editor:** ![](./badges/emacs-26.3-lightseagreen.svg) ![](./badges/nano-4.8-lightseagreen.svg) ![](./badges/vim-8.1-lightseagreen.svg)
* **Package Manager:** ![](./badges/apt-2.0.9-lightseagreen.svg) ![](./badges/dpkg-1.19.7-lightseagreen.svg) ![](./badges/pip-20.0.2-lightseagreen.svg)
* **Programming Language:** ![](./badges/GCC-9.4.0-lightseagreen.svg) ![](./badges/MATLAB-R2023a-lightseagreen.svg) ![](./badges/Python-3.8.10-lightseagreen.svg)

:::

::: {tab-item} 7.3.2

[![](badges/release-7.3.2-blue.svg)](https://cloud.sdu.dk/app/jobs/create?app=freesurfer&version=7.3.2)
![type](badges/type-VDE-yellow.svg)
![access](badges/access-restricted-red.svg)
* **Operating System:** ![](./badges/Ubuntu-20.04-lightseagreen.svg)
* **Terminal:** ![](./badges/tmux-3.0a-lightseagreen.svg)
* **Shell:** ![](./badges/bash-5.0.17-lightseagreen.svg)
* **Editor:** ![](./badges/emacs-26.3-lightseagreen.svg) ![](./badges/nano-4.8-lightseagreen.svg) ![](./badges/vim-8.1-lightseagreen.svg)
* **Package Manager:** ![](./badges/apt-2.0.9-lightseagreen.svg) ![](./badges/dpkg-1.19.7-lightseagreen.svg) ![](./badges/pip-20.0.2-lightseagreen.svg)
* **Programming Language:** ![](./badges/GCC-9.4.0-lightseagreen.svg) ![](./badges/MATLAB-R2022b-lightseagreen.svg) ![](./badges/Python-3.8.10-lightseagreen.svg)

:::

::::

[FreeSurfer](https://surfer.nmr.mgh.harvard.edu/) is a software package for the analysis and visualization of neuroimaging data from cross-sectional and longitudinal studies.

FreeSurfer provides full processing streams for structural and functional MRI and includes tools for linear and nonlinear registration, cortical and subcortical segmentation, cortical surface reconstruction, statistical analysis of group morphometry, diffusion MRI, PET analysis, and much more.

## Initialization

For information on how to use the *Initialization* parameter, please refer to the [Initialization - Bash script](../hands-on/init-sh.md), [Initialization - Conda packages](../hands-on/init-conda.md), and [Initialization - pip packages](../hands-on/init-pip.md) section of the documentation.

## FreeSurfer license

The user can import a personal license file using the *FreeSurfer license* optional parameter.

## MATLAB network license

Depending on the user institution, it is possible to request access to a license server using the *Select MATLAB license server* optional parameter. The license server must be added to an active project by means of a [grant application](../guide/resources-grant.md).
Project admins can restrict access to the license as discussed [here](../guide/project-overview.md#license-management).

For more information about MATLAB, check the related documentation [here](matlab.md).
