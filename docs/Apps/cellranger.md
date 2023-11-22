# Cell Ranger

:::: {tab-set}

::: {tab-item} 7.1.0

[![Cell Ranger](badges/release-7.1.0-blue.svg)](https://cloud.sdu.dk/app/applications?tag=Cell%20Ranger&itemsPerPage=25&page=0)
![type](badges/type-batch-yellow.svg)
![access](badges/access-open-green.svg)

* **Operating System:** ![](./badges/AlmaLinux-8.7-lightseagreen.svg)
* **Terminal:** ![](./badges/tini-0.19.0-lightseagreen.svg) ![](./badges/tmux-2.7-lightseagreen.svg)
* **Shell:** ![](./badges/bash-4.4.20-lightseagreen.svg) ![](./badges/fish-3.3.1-lightseagreen.svg) ![](./badges/zsh-5.5.1-lightseagreen.svg)
* **Editor:** ![](./badges/emacs-26.1-lightseagreen.svg) ![](./badges/nano-2.9.8-lightseagreen.svg) ![](./badges/vim-8.0-lightseagreen.svg)
* **Package Manager:** ![](./badges/dnf-4.7.0-lightseagreen.svg) ![](./badges/npm-6.14.11-lightseagreen.svg) ![](./badges/pip-9.0.3-lightseagreen.svg) ![](./badges/rpm-4.14.3-lightseagreen.svg) ![](./badges/yum-4.7.0-lightseagreen.svg)
* **Programming Language:** ![](./badges/GCC-8.5.0-lightseagreen.svg) ![](./badges/OpenJDK-1.8.0-lightseagreen.svg) ![](./badges/Python-3.6.8-lightseagreen.svg) ![](./badges/Python-2.7.18-lightseagreen.svg)
* **Utility:** ![](./badges/Lmod-8.7-lightseagreen.svg)

:::

::: {tab-item} 7.0.1

[![Cell Ranger](badges/release-7.0.1-blue.svg)](https://cloud.sdu.dk/app/applications?tag=Cell%20Ranger&itemsPerPage=25&page=0)
![type](badges/type-batch-yellow.svg)
![access](badges/access-open-green.svg)

:::

::: {tab-item} 6.1.1

[![Cell Ranger](badges/release-6.1.1-blue.svg)](https://cloud.sdu.dk/app/applications?tag=Cell%20Ranger&itemsPerPage=25&page=0)
![type](badges/type-batch-yellow.svg)
![access](badges/access-open-green.svg)

:::

::: {tab-item} 5.0.1

[![Cell Ranger](badges/release-5.0.1-blue.svg)](https://cloud.sdu.dk/app/applications?tag=Cell%20Ranger&itemsPerPage=25&page=0)
![type](badges/type-batch-yellow.svg)
![access](badges/access-open-green.svg)

:::

::: {tab-item} 3.1.0

[![Cell Ranger](badges/release-3.1.0-blue.svg)](https://cloud.sdu.dk/app/applications?tag=Cell%20Ranger&itemsPerPage=25&page=0)
![type](badges/type-batch-yellow.svg)
![access](badges/access-open-green.svg)

:::

::::

Cell Ranger is a toolset of analysis pipelines from [10X Genomics](https://www.10xgenomics.com/) that process Chromium single-cell RNA-seq output to align reads, generate feature-barcode matrices and perform clustering and gene expression analysis.

For more information, check [here](https://support.10xgenomics.com/single-cell-gene-expression/software/pipelines/latest/what-is-cell-ranger).

<details>
<summary><b>Cell Ranger Utilities</b></summary>

- [![aggr](badges/aggr-yellowgreen.svg)](https://cloud.sdu.dk/app/jobs/create?app=cellranger-aggr&version=7.0.1)
- [![count](badges/count-yellowgreen.svg)](https://cloud.sdu.dk/app/jobs/create?app=cellranger-count&version=7.0.1)
- [![mat2csv](badges/mat2csv-yellowgreen.svg)](https://cloud.sdu.dk/app/jobs/create?app=cellranger-mat2csv&version=7.0.1)
- [![mkfastq](badges/mkfastq-yellowgreen.svg)](https://cloud.sdu.dk/app/jobs/create?app=cellranger-mkfastq&version=7.0.1)
- [![mkgtf](badges/mkgtf-yellowgreen.svg)](https://cloud.sdu.dk/app/jobs/create?app=cellranger-mkgtf&version=7.0.1)
- [![mkref](badges/mkref-yellowgreen.svg)](https://cloud.sdu.dk/app/jobs/create?app=cellranger-mkref&version=7.0.1)
- [![mkvdjref](badges/mkvdjref-yellowgreen.svg)](https://cloud.sdu.dk/app/jobs/create?app=cellranger-mkvdjref&version=7.0.1)
- [![multi](badges/multi-yellowgreen.svg)](https://cloud.sdu.dk/app/jobs/create?app=cellranger-multi&version=7.0.1)
- [![reanalyze](badges/reanalyze-yellowgreen.svg)](https://cloud.sdu.dk/app/jobs/create?app=cellranger-reanalyze&version=7.0.1)
- [![targeted-compare](badges/targeted-compare-yellowgreen.svg)](https://cloud.sdu.dk/app/jobs/create?app=cellranger-targeted-compare&version=7.0.1)
- [![terminal](badges/terminal-yellowgreen.svg)](https://cloud.sdu.dk/app/jobs/create?app=cellranger-terminal&version=7.0.1)
- [![testrun](badges/testrun-yellowgreen.svg)](https://cloud.sdu.dk/app/jobs/create?app=cellranger-testrun&version=7.0.1)
- [![vdj](badges/vdj-yellowgreen.svg)](https://cloud.sdu.dk/app/jobs/create?app=cellranger-vdj&version=7.0.1)
</details>

## Terminal session

The _Cell Ranger: terminal_ utility allows the user run the different Cell Ranger pipelines via command line by clicking

{{ btn_open_terminal }}

## User interface

When available, the `--uiport=3600` option enables the pipeline's visual user interface (UI), accessible through the button

{{ btn_open_interface }}

``` {note}
The UI port must be ``3600``.
```
