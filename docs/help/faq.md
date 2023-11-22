# Frequently Asked Questions

```{eval-rst}
.. raw:: html

    <style>
        blockquote {
           border-color: white;
           background-color: white;
        }
        .toggle-header p {font-size: 20px;}
        .toggle-header strong {color: black;}
        .toggle-header:after {
            content: " ╋";
            color: var(--main-color);;
        }
        .toggle-header.open:after {
            content: " ━";
        }
        @media screen and (max-width: 768px) {
        .toggle-header p {font-size: 15px;}
        }
    </style>
```


```{eval-rst}
.. toggle-header::
    :header: **1.** Missing files when extracting my zip on UCloud

     If you are using MacOS, be sure to not use the compress (Archive Utility) option when zipping. Archive Utility cannot handle more than 65535 files per zip or files larger than 4 GB. It will not fail zipping, but the zip file will be corrupt. Instead use the zip command from the terminal.
```

<br>

```{eval-rst}
.. toggle-header::
    :header: **2.** Cannot extract downloaded zip of folders from UCloud

     UCloud uses zip64 to zip folders for download. This is because many of the users have files larger than 4 GB and without zip64 this would have been the limit. If the extraction happens on MacOS, use the zip command from the terminal instead of Archive Utility. If on Windows try out `7zip <https://www.7-zip.org/>`__ instead.
```

<br>

```{eval-rst}
.. toggle-header::
    :header: **3.** How can I use Conda on UCloud?

     Conda is already pre-installed in `JupyterLab <../Apps/jupyter-lab.html>`__ and `PyTorch <../Apps/pytorch.html>`__. Nonetheless, it is also possible to install and use Conda without root privileges via the terminal window of another UCloud interactive app.

     For more information check `here <../hands-on/conda-setup.html>`__.
```

<br>

```{eval-rst}
.. toggle-header::
    :header: **4.** Incorrect Python interpreter when loading a Conda environment created in JupyterLab

     This is a known `bug <https://github.com/conda/conda/issues/9392>`__ of Conda.
     One workaround consists in installing at least one package when the environment is created, as show in these `examples <../Apps/jupyter-lab.html#conda-virtual-environment>`__. Another solution is to create a file named ``.condarc`` in the ``$HOME`` folder, with the following lines of code:

     .. code-block:: yaml

        create_default_packages:
          - python
```

<br>

```{eval-rst}
.. toggle-header::
    :header: **5.** How can I synchronize GitHub/GitLab/Bitbucket repositories stored in UCloud?

     It is possible to synchronize remote repositories using any interactive app (e.g., Terminal, Coder, RStudio, JupyterLab). In fact, all these apps have Git and an SSH client pre-installed. You should first create a `deploy key <https://docs.github.com/en/free-pro-team@latest/developers/overview/managing-deploy-keys>`__ for the remote repository and then set up your Git credentials inside UCloud, e.g. with a script as this one:

     .. code-block:: bash

        #!/bin/bash

        eval `ssh-agent -s`
        ssh-add /work/ssh/id_rsa
        git config --global user.name "add here your name"
        git config --global user.email "add here your email"
        bash -i

     where ``id_rsa`` is your SSH private key. The corresponding public key must be stored on the remote repository.
```

<br>

```{eval-rst}
.. toggle-header::
    :header: **6.** Is it possible to run Docker containers on UCloud?

     It is not possible for now to install and run Docker within an interactive application hosted on UCloud. Nevertheless, the user can install the `udocker <https://github.com/indigo-dc/udocker>`__ command line interface to execute simple containers in user space, without root privileges.
     In a future release of UCloud we will allow users to run their own containers.

     Alternatively, it is possible to run Docker containers inside a `virtual machine <../Apps/vm_apps.html>`__.
```

<br>

```{eval-rst}
.. toggle-header::
    :header: **7.** Can I connect to UCloud via SSH from my laptop?

     It is possible to connect to UCloud via SSH using the `Rsync Server <../Apps/rsync.html#synchronize-local-data>`__ and `Terminal <../Apps/terminal.html#attach-a-public-ip>`__ applications.
```

<br>

```{eval-rst}
.. toggle-header::
    :header: **8.** How shall I process sensitive data on UCloud?

     If you are part of SDU and work with sensitive data, you should consult the procedure reported `here <https://www.sdu.dk/en/anmeldelse>`__.

     Data stored on UCloud is conditioned to the SDU eScience `data processing agreement <https://legal.cloud.sdu.dk/terms/data-processing-terms>`__.
```

<br>

```{eval-rst}
.. toggle-header::
    :header: **9.** I am a bachelor/master/PhD student - How do I apply for a project on UCloud?

     Students are not allowed to apply for projects. In this case the supervisor should submit a `grant application <../guide/resources-grant.html>`__ for the project and invite the student, once it has been approved.
```

<br>

```{eval-rst}
.. toggle-header::
    :header: **10.** How shall I acknowledge and/or cite UCloud in my publications?

     If you publish research results from computations done on UCloud, we recommend to rephrase the following sentence in the final acknowledgments:

     .. raw:: html

        <em>All/part of the computation done for this project was performed on the</em> <a href="https://docs.cloud.sdu.dk"><em>UCloud</em></a> <em>interactive HPC system, which is managed by the eScience Center at the University of Southern Denmark.</em>
```

<br>

```{eval-rst}
.. toggle-header::
    :header: **11.** Is it possible to run software for Windows on UCloud?

     It is currently not possible to run software developed for Microsoft Windows operating system. However, in the future we will allow to deploy Windows virtual machines for this purpose.
```
