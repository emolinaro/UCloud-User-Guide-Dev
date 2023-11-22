# Initialization - Conda packages

For any app that implements the `Conda` package manager, a Conda environment file (`*.yml/*.yaml`) can be passed to Conda package manager during app initialization using the optional parameter *Initialization*.

When the application is initalized, Conda will create the environment as specified in the environment file.

This is the equivelant of running `conda env create --file` with the selected file as input.

Pip dependencies can be installed through the yaml file as well. See below for an example.

Example yaml file:

```yaml
name: base
channels:
  - conda-forge
  - defaults
  - numba

dependencies:
  - conda-forge::keras=2.3.1
  - conda-forge::matplotlib=3.2.0
  - conda-forge::numpy=1.18.1
  - conda-forge::pandas=1.0.2
  - conda-forge::seaborn=0.10.0
  - numba::numba=0.48.0
  - pip:
    - plotly==4.5.4
```

``` {Note}
Please note that for some apps, this option might be called *Dependencies* or *Additional Dependencies*.
```
