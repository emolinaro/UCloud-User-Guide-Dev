# Rsync Server

:::: {tab-set}

::: {tab-item} 3.2.7

[![](badges/release-3.2.7-blue.svg)](https://cloud.sdu.dk/app/jobs/create?app=rsync-server&version=3.2.7)
![type](badges/type-interactive-yellow.svg)
![access](badges/access-open-green.svg)
* **Operating System:** ![](./badges/Ubuntu-22.10-lightseagreen.svg)
* **Terminal:** ![](./badges/tini-0.19.0-lightseagreen.svg) ![](./badges/tmux-3.3a-lightseagreen.svg)
* **Shell:** ![](./badges/bash-5.2.2-lightseagreen.svg) ![](./badges/fish-3.5.1-lightseagreen.svg) ![](./badges/zsh-5.9-lightseagreen.svg)
* **Editor:** ![](./badges/emacs-27.1-lightseagreen.svg) ![](./badges/nano-6.4-lightseagreen.svg) ![](./badges/vim-9.0-lightseagreen.svg)
* **Package Manager:** ![](./badges/apt-2.5.3-lightseagreen.svg) ![](./badges/dpkg-1.21.9-lightseagreen.svg) ![](./badges/npm-8.18.0-lightseagreen.svg) ![](./badges/pip-22.2-lightseagreen.svg)
* **Programming Language:** ![](./badges/GCC-12.2.0-lightseagreen.svg) ![](./badges/Python-3.10.7-lightseagreen.svg) ![](./badges/Python-2.7.18-lightseagreen.svg)
* **Utility:** ![](./badges/Lmod-8.7-lightseagreen.svg)
* **Extension:** ![](./badges/OpenMPI-4.1.4-lightseagreen.svg)

:::

::: {tab-item} 3.1.3

[![](badges/release-3.1.3-blue.svg)](https://cloud.sdu.dk/app/jobs/create?app=rsync-server&version=3.1.3b)
![type](badges/type-interactive-yellow.svg)
![access](badges/access-open-green.svg)
* **Operating System:** ![](./badges/Debian-10-lightseagreen.svg)
* **Shell:** ![](./badges/bash-5.0.3-lightseagreen.svg)
* **Editor:** ![](./badges/nano-3.2-lightseagreen.svg) ![](./badges/vim-8.1-lightseagreen.svg)
* **Package Manager:** ![](./badges/apt-1.8.2.3-lightseagreen.svg) ![](./badges/dpkg-1.19.7-lightseagreen.svg)
* **Programming Language:** ![](./badges/Python-2.7.16-lightseagreen.svg)

:::

::::

This application is used to deploy an rsync server, which is a utility to efficiently transfer and synchronize files and directories between two different systems.

For more information about rsync, check the official [man page](https://linux.die.net/man/1/rsync).

## Rsync settings

By default, the rsync daemon settings are specified in `/etc/rsyncd.conf`. A new configuration file can be uploaded using the corresponding optional parameter.

## Synchronize local data

Rsync is configured by default to use a remote-shell transport layer protocol, such as SSH or RSH.
The user must upload an SSH _public key_, which will be used to encrypt and secure transfer data from a remote host.
For more information check [here](general_settings.md#configure-ssh-access).

Once the application is launched, a new panel will appear in the job progress view showing the SSH login command and the port for SSH client connections. The SSH port value is randomly generated.

To connect to the rsync server from a remote host and transfer data, one can use the command:

```console
user@remote_host:~$ rsync -avP -e "ssh -i ~/.ssh/id_rsa -p <port>" ./data/ ucloud@ssh.cloud.sdu.dk:/work/data
```

where `./data` is the path to the data folder and `~/.ssh/id_rsa` the path to the matched SSH *private key* on the remote host.
The SSH port (`<port>`) must be replaced with the value reported in the *SSH access* panel.

``` {note}
The default user on the remote server must be `ucloud`. The data must be sync to a folder within the default working path `/work`.
```
