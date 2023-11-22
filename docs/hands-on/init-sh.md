# Initialization - Bash script

For any app with a `Bash` shell, a bash script can be loaded (`*.sh`) during app initialization using the optional parameter *Initialization*.

The bash script should include a shebang (`#!/usr/bin/env bash`) and have the `.sh` file extension.

The script will be executed when the app is initialized, and can be used to install relevant packages or configuration.

The script in the first tab (**Installing R-packages**) includes the installation of R packages. The second and the third tab show how to install the mariadb-server, with the apt package manager (for Debian/Ubuntu based distributions) or with the yum package manger (for Red Hat based distributions), respectively.


Example bash scripts:
:::: {tab-set}

::: {tab-item} Installing R-packages
```shell
#!/bin/bash

sudo apt-get update
sudo apt-get install -y libssl-dev liblzma-dev libbz2-dev libicu-dev libxml2-dev libglpk-dev
sudo apt-get clean

R -e "install.packages('BiocManager', repos='http://cran.us.r-project.org'); \
    update.packages(ask=F); \
    BiocManager::install(ask=F); \
    BiocManager::install(c('dplyr','plotly'),ask=F)"

R -e "library(BiocManager); BiocManager::install(c('matrixStats','igraph','parallel', \
    'lattice','plyr','gplots','data.table','clusterProfiler','org.Hs.eg.db','STRINGdb', \
    'jsonlite','shinydashboard','shinyBS'    ,'limma'),ask=F)"

R -e "library(BiocManager); BiocManager::install(c('biomaRt'),ask=F)"
```

:::

::: {tab-item} using apt

```shell
#!/usr/bin/env bash
sudo apt update
sudo apt install -y mariadb-server
```

:::

::: {tab-item} using yum

```shell
#!/usr/bin/env bash
sudo yum install -y mariadb-server
```

:::

::::

``` {Note}
Please note that for some apps, this option might be called *Dependencies* or *Additional Dependencies*.
```
