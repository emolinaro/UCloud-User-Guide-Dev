# Space Ranger

[![](badges/release-2.0.1-blue.svg)](https://cloud.sdu.dk/app/applications?tag=Space%20Ranger&itemsPerPage=25&page=0)
![type](badges/type-batch-yellow.svg)
![access](badges/access-open-green.svg)
* **Operating System:** ![](./badges/AlmaLinux-8.7-lightseagreen.svg)
* **Terminal:** ![](./badges/tini-0.19.0-lightseagreen.svg) ![](./badges/tmux-2.7-lightseagreen.svg)
* **Shell:** ![](./badges/bash-4.4.20-lightseagreen.svg) ![](./badges/fish-3.3.1-lightseagreen.svg) ![](./badges/zsh-5.5.1-lightseagreen.svg)
* **Editor:** ![](./badges/emacs-26.1-lightseagreen.svg) ![](./badges/nano-2.9.8-lightseagreen.svg) ![](./badges/vim-8.0-lightseagreen.svg)
* **Package Manager:** ![](./badges/dnf-4.7.0-lightseagreen.svg) ![](./badges/npm-6.14.11-lightseagreen.svg) ![](./badges/pip-9.0.3-lightseagreen.svg) ![](./badges/rpm-4.14.3-lightseagreen.svg) ![](./badges/yum-4.7.0-lightseagreen.svg)
* **Programming Language:** ![](./badges/GCC-8.5.0-lightseagreen.svg) ![](./badges/OpenJDK-1.8.0-lightseagreen.svg) ![](./badges/Python-3.6.8-lightseagreen.svg) ![](./badges/Python-2.7.18-lightseagreen.svg)
* **Utility:** ![](./badges/Lmod-8.7-lightseagreen.svg)

Visium Spatial Gene Expression is a molecular profiling solution for classifying tissue based on total mRNA.
Space Ranger is a set of analysis pipelines that process Visium Spatial Gene Expression data with brightfield and fluorescence microscope images. Space Ranger allows users to map the whole transcriptome in formalin fixed paraffin embedded (FFPE) and fresh-frozen tissues to discover novel insights into normal development, disease pathology, and clinical translational research.

For more information, check [here](https://support.10xgenomics.com/spatial-gene-expression/software/pipelines/latest/what-is-space-ranger).

<details>
<summary><b>Space Ranger Utilities</b></summary>

- [![aggr](badges/aggr-yellowgreen.svg)](https://cloud.sdu.dk/app/jobs/create?app=spaceranger-aggr&version=2.0.1)
- [![count](badges/count-yellowgreen.svg)](https://cloud.sdu.dk/app/jobs/create?app=spaceranger-count&version=2.0.1)
- [![mat2csv](badges/mat2csv-yellowgreen.svg)](https://cloud.sdu.dk/app/jobs/create?app=spaceranger-mat2csv&version=2.0.1)
- [![mkfastq](badges/mkfastq-yellowgreen.svg)](https://cloud.sdu.dk/app/jobs/create?app=spaceranger-mkfastq&version=2.0.1)
- [![mkgtf](badges/mkgtf-yellowgreen.svg)](https://cloud.sdu.dk/app/jobs/create?app=spaceranger-mkgtf&version=2.0.1)
- [![mkref](badges/mkref-yellowgreen.svg)](https://cloud.sdu.dk/app/jobs/create?app=spaceranger-mkref&version=2.0.1)
- [![targeted-compare](badges/targeted-compare-yellowgreen.svg)](https://cloud.sdu.dk/app/jobs/create?app=spaceranger-targeted-compare&version=2.0.1)
- [![targeted-depth](badges/targeted-depth-yellowgreen.svg)](https://cloud.sdu.dk/app/jobs/create?app=spaceranger-targeted-depth&version=2.0.1)
- [![terminal](badges/terminal-yellowgreen.svg)](https://cloud.sdu.dk/app/jobs/create?app=spaceranger-terminal&version=2.0.1)
- [![testrun](badges/testrun-yellowgreen.svg)](https://cloud.sdu.dk/app/jobs/create?app=spaceranger-testrun&version=2.0.1)
</details>

## Terminal session

The _Space Ranger: terminal_ utility allows the user run the different Space Ranger pipelines via command line by clicking

{{ btn_open_terminal }}

## User interface

When available, the `--uiport=3600` option enables the pipeline's visual user interface (UI), accessible through the button

{{ btn_open_interface }}

``` {note}
The UI port must be ``3600``.
```
