# Setup Conda on UCloud

The [Conda](https://docs.conda.io/projects/conda/en/latest/index.html) package and environment management system is already included in few applications available on UCloud (see, e.g., [JupyerLab](../Apps/jupyter-lab.md) and [PyTorch](../Apps/pytorch.md)).

For more general uses of Conda and its powerful package manager it is convenient to create a local installation and save it in a UCloud project.

Conda is included in all versions of Anaconda and Miniconda. For example, to install the latest version of Miniconda, just start any interactive app on UCloud, such as [Terminal](../Apps/terminal.md), and run the following shell commands:

```console
$ curl -s -L -o /tmp/miniconda_installer.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
$ bash /tmp/miniconda_installer.sh -b -f -p /work/miniconda3
```

The installation directory, in this case `miniconda3`, must be created in the *default working tree*, so that it is available in the [job output folder](../guide/submitting.md#job-completed) for later use.

Conda can be added to the search path with the command:

```console
$ eval "$(/work/miniconda3/bin/conda shell.bash hook)"
```

or

```console
$ sudo ln -s /work/miniconda3/bin/conda /usr/bin/conda
```

Both Conda [packages](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/packages.html) and [environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) are then installed in `/work/miniconda3`.

To initialize the current shell for use with Conda, run:

```console
$ conda init
```
