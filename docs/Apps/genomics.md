# Genomics Sandbox


:::: {tab-set}

::: {tab-item} 2023-03-01

[![](badges/release-2023-03-01-blue.svg)](https://cloud.sdu.dk/app/jobs/create?app=genomics&version=2023.03.01)
![type](badges/type-VDE-yellow.svg)
![access](badges/access-open-green.svg)

* **Operating System:** ![](./badges/Ubuntu-22.10-lightseagreen.svg)
* **Terminal:** ![](./badges/tini-0.19.0-lightseagreen.svg)
* **Shell:** ![](./badges/bash-5.2.2-lightseagreen.svg)
* **Editor:** ![](./badges/emacs-27.1-lightseagreen.svg) ![](./badges/nano-6.4-lightseagreen.svg) ![](./badges/vim-9.0-lightseagreen.svg)
* **Package Manager:** ![](./badges/apt-2.5.3-lightseagreen.svg) ![](./badges/conda-22.11.1-lightseagreen.svg) ![](./badges/dpkg-1.21.9-lightseagreen.svg) ![](./badges/npm-8.19.2-lightseagreen.svg) ![](./badges/pip-23.0.1-lightseagreen.svg)
* **Programming Language:** ![](./badges/GCC-12.2.0-lightseagreen.svg) ![](./badges/Python-3.10.8-lightseagreen.svg)

:::

::: {tab-item} 2022-08-01

[![](badges/release-2022-08-01-blue.svg)](https://cloud.sdu.dk/app/jobs/create?app=genomics&version=2022.08.01)
![type](badges/type-VDE-yellow.svg)
![access](badges/access-open-green.svg)

* **Operating System:** ![](./badges/Ubuntu-22.04-lightseagreen.svg)
* **Terminal:** ![](./badges/tini-0.19.0-lightseagreen.svg)
* **Shell:** ![](./badges/bash-5.1.16-lightseagreen.svg)
* **Editor:** ![](./badges/emacs-27.1-lightseagreen.svg) ![](./badges/nano-6.2-lightseagreen.svg) ![](./badges/vim-8.2-lightseagreen.svg)
* **Package Manager:** ![](./badges/apt-2.4.5-lightseagreen.svg) ![](./badges/conda-4.13.0-lightseagreen.svg) ![](./badges/dpkg-1.21.1-lightseagreen.svg) ![](./badges/npm-8.5.5-lightseagreen.svg) ![](./badges/pip-22.2.2-lightseagreen.svg)
* **Programming Language:** ![](./badges/GCC-11.2.0-lightseagreen.svg) ![](./badges/Python-3.9.13-lightseagreen.svg)

:::

::::

In this app you will find material for the Genomics sandbox of the **[Health Data Science sandbox](https://hds-sandbox.github.io)**. This contains courses you can learn from, datasets and tools you can work with for your own research/learning purposes. Each course item of this sandbox is based on JupyterLab. JupyterLab is a web-based integrated development environment for Jupyter notebooks, code, and data. Usually, each item includes a dedicated webpage with additional information, guides, and material.

## Available material

Items are periodically added to this app and can be chosen from the menu. Each item can a course, a setup to work with specific software, a research example, and comes with all necessary packages already installed, notebooks with code and explanations, and a dedicated webpage with additional material (notes, slides, recordings, ...).

### Courses

 The available courses are:

| **Course Name**   | **Description**   | **Link**   | **Programming Language** |
| ---------------   | ---------------   | :--------: | ------------------------ |
| **Introduction to NGS <br/> Data Analysis**  | <div style="text-align: left"> A one-week course to introduce NGS data, from data alignment to bioinformatics analysis </div> | [Webpage](https://hds-sandbox.github.io/NGS_summer_course_Aarhus/) | Python, R, Bash |
| **Introduction to <br/> Population Genomics**  | <div style="text-align: justify"> A course introducing and applying bioinformatic tools to perform a whole population genomics analysis </div> | [Webpage](https://hds-sandbox.github.io/NGS_summer_course_Aarhus/) | Python, R, Bash |
| **Introduction to GWAS**                 | <div style="text-align: justify">  An introductory course in Genome-Wide Association Studies                                               </div> | [Webpage](https://hds-sandbox.github.io/GWAS_course/) | R, Bash |

### Tools

The available tools are:

| **Tool Name**     | **Description** |  **Links**    | **Programming language** |
| ----------------- | --------------- | ------------- | ------------------------ |
| **Integrative Genomics Viewer**     | <div style="text-align: justify"> A High-performance, easy-to-use, interactive tool for the visual exploration of genomic data. It supports flexible integration of all the common types of genomic data and metadata, investigator-generated or publicly available. </div> | [Official Manual](https://igvteam.github.io/igv-webapp/) | Interactive User Interface |

## Choosing an item

You can choose a course or a tool from the drop down menu accessible in the job submission page (red circle in the figure below).
<br>

<img src="figs/app_setup.png" alt="drawing" width="85%" align="center">

<br>

``` {note}
The App needs to download data and packages. Depending on the selected course/tool, this can take some time. See below how to reuse data and avoid long waiting times (you still need to download data the first time you run the app).
```

### Available options

You can use data and notebooks running in a previous session of the app, otherwise, all the datasets the notebooks will be downloaded every time a new session is started.

To choose the data from previous sessions, click on *Add folder* (red circle in the figure below). Then, you need to select your latest session of the sandbox (inside the folder `Jobs/Genomics Sandbox`, as shown in the example below) and choose the folder you need. Accepted folders are `Data` and `Notebooks` (such as the two folders chosen in the figure below).
<br>

<img src="figs/add_folder.png" alt="drawing" width="85%" align="center">

<br>

## Download course data and notebooks

Each course is open-source and the datasets are freely available. Here you have the link to all repositories to download the datasets.

| **Course Name**                          | **Data Repository** |
| ---------------------------------------- | ------------------- |
| **Introduction to NGS Data Analysis**    | [Link](https://zenodo.org/record/7670370)          |
| **Introduction to Population Genomics**  | [Link](https://zenodo.org/record/7670839)          |
| **Introduction to GWAS**                 | [Link](https://github.com/hds-sandbox/GWAS_course)          |

## Download generated data

You can easily download the generated files by right-clicking the selected files in JupyterLab and choosing download (see figure below).
<br>

<img src="figs/download.png" alt="drawing" width="85%" align="center">

<br>
