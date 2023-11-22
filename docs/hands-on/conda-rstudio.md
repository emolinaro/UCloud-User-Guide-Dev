# Use Conda in RStudio

For those use cases where an R project depends on some Python packages it is possible to integrate a [local installation of Conda](conda-setup.md) directly into the [RStudio](../Apps/rstudio.md) app.
This integration is done via the `renv` and `reticulate` packages of R.

In the following example, the Miniconda installation directory, say `miniconda3`, is mounted inside an instance of RStudio.
In order to use Conda, the `conda` binary must be added to the search path from the RStudio terminal interface:

```console
$ sudo ln -s /work/miniconda3/bin/conda /usr/bin/conda
```

As a first step one must create a new Conda environment, called `py_env`, which includes a Python package, e.g. `numpy`:

```console
$ conda create -n py_env numpy
```

Optionally, one can activate the environment to install additional packages with the commands:

```console
$ conda init && bash -i
```

and

```console
$ conda activate py_env
```

Next, it is necessary to create a new folder to install the R project which has to be integrated with the Conda environment created earlier:

```console
$ mkdir /work/my_project
```

Finally, the R project is initialized directly in the RStudio console:

```R
setwd('/work/my_project')
renv::init()
Sys.setenv(RENV_PATHS_CACHE = '/work/my_project/renv/cache')
renv::use_python(type = 'conda', name = 'py_env')
```

where the `renv::use_python` function takes as argument the name of the Conda environment. The content of `my_project` is available in the job output folder for later use,  after the RStudio instance is stopped.

To check that the `renv` environment is correctly configured, one can run the following commands:

```R
library('reticulate')
np <- import('numpy')
np$arange(10)
```

To automate this workflow in a new RStudio instance, the user must add both the Miniconda and R project folders and use the optional *Dependencies* parameter to run a configuration script, such as the following:

```bash
#!/bin/bash

sudo ln -s /work/miniconda3/bin/conda /usr/bin/conda

echo "Sys.setenv(RENV_PATHS_CACHE = '/work/my_project/renv/cache')" > ~/.Rprofile

echo "renv::load(project = '/work/my_project')" >> ~/.Rprofile

printf "Done.\n"
```
