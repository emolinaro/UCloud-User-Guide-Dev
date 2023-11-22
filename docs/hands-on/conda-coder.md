# Use Conda in Coder

It is possible to use multiple Python interpreters within the same instance of the [Coder Python](../Apps/coder.md) app.

For example, consider a [local installation of Miniconda](conda-setup.md), say `miniconda3`, mounted inside the app.
From the app terminal interface add Conda to the search path via:

```console
$ eval "$(/work/miniconda3/bin/conda shell.bash hook)"
```

:::{tip}
(base) <span style="color: red;"><b>ucloud</b></span>:<span style="color: blue;"><b>/work</b></span>$
:::

The list of Conda environments is returned by:

```console
$ conda env list
```

:::{tip}
\# conda environments:

\#

base &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; * /work/miniconda3

py_env &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; /work/miniconda3/envs/py_env
:::

So, one of the environments can be activated as in the example below:

```console
$ conda activate py_env
```

:::{tip}
(py_env) <span style="color: red;"><b>ucloud</b></span>:<span style="color: blue;"><b>/work</b></span>$
:::

To use the Python interpreter which corresponds to the selected environment, repeat the following steps from the app interface:

- Press `Ctrl/Cmd + Shift + P` or select the menu `View -> Command Palette...`
- Execute the command `> Python: Select Intepreter`
- Click on `Enter intepreter path...`
- Add the full path of the Python command: `/work/miniconda3/envs/py_env/bin/python`
