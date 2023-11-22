# Initialization - pip packages

For any app that implements the `pip` package manager, a list of packages can be installed during app initialization using the optional parameter *Initialization*.

The packages will be installed via the `pip` command line Python package manager.

The user should provide a list of pip packages to be installed as a text file (`.txt`).

This will run `pip install -r` with the text file as input when the application is initialized.

Example text file:

```text
keras==2.3.1
matplotlib==3.2.0
numpy==1.18.1
pandas==1.0.2
plotly==4.5.4
seaborn==0.10.0
```

``` {Note}
Please note that for some apps, this option might be called *Dependencies* or *Additional Dependencies*.
```
