# MySQL Server

:::: {tab-set}

::: {tab-item} 8.0.32

[![release](badges/release-8.0.32-blue.svg)](https://cloud.sdu.dk/app/jobs/create?app=mysql-server&version=8.0.32)
![type](badges/type-interactive-yellow.svg)
![access](badges/access-open-green.svg)
* **Operating System:** ![](./badges/OracleLinux-8.8-lightseagreen.svg)
* **Terminal:** ![](./badges/tmux-2.7-lightseagreen.svg)
* **Shell:** ![](./badges/bash-4.4.20-lightseagreen.svg)
* **Editor:** ![](./badges/emacs-26.1-lightseagreen.svg) ![](./badges/nano-2.9.8-lightseagreen.svg) ![](./badges/vim-8.0-lightseagreen.svg)
* **Package Manager:** ![](./badges/dnf-4.7.0-lightseagreen.svg) ![](./badges/rpm-4.14.3-lightseagreen.svg) ![](./badges/yum-4.7.0-lightseagreen.svg)
* **Programming Language:** ![](./badges/Python-3.9.16-lightseagreen.svg)
* **Database:** ![](./badges/MySQL-8.0.32-lightseagreen.svg)

:::

::: {tab-item} 8.0.24

[![release](badges/release-8.0.24-blue.svg)](https://cloud.sdu.dk/app/jobs/create?app=mysql-server&version=8.0.24a)
![type](badges/type-interactive-yellow.svg)
![access](badges/access-open-green.svg)
* **Operating System:** ![](./badges/Fedora-8.4-lightseagreen.svg)
* **Terminal:** ![](./badges/tmux-2.7-lightseagreen.svg)
* **Shell:** ![](./badges/bash-4.4.20-lightseagreen.svg)
* **Editor:** ![](./badges/emacs-26.1-lightseagreen.svg) ![](./badges/nano-2.9.8-lightseagreen.svg) ![](./badges/vim-8.0-lightseagreen.svg)
* **Package Manager:** ![](./badges/dnf-4.4.2-lightseagreen.svg) ![](./badges/rpm-4.14.3-lightseagreen.svg) ![](./badges/yum-4.4.2-lightseagreen.svg)
* **Programming Language:** ![](./badges/Python-3.6.8-lightseagreen.svg)
* **Database:** ![](./badges/MySQL-8.0.24-lightseagreen.svg)

:::

::::

MySQL is an open-source relational database management system based on SQL - Structured Query Language.

For more information, check the official documentation [here](https://dev.mysql.com/doc/refman/8.0/en/).

## Initialization

For information on how to use the *Initialization* parameter, please refer to the [Initialization - Bash script](../hands-on/init-sh.md) section of the documentation.

## Create a new server

The app requires to set the *Database* parameter, which is used to import the MySQL database folder from a UCloud workspace.
If the folder is empty, a new database will be initialized.
In this case, after the initialization procedure is completed, the following lines will be displayed in the output logs:

```xml
[Entrypoint] GENERATED ROOT PASSWORD: <root_temporary_password>

[Entrypoint] ignoring /docker-entrypoint-initdb.d/*

[Entrypoint] Server shut down
[Entrypoint] Setting root user as expired. Password will need to be changed before database can be used.

[Entrypoint] MySQL init process done. Ready for start up.

[Entrypoint] Starting MySQL 8.0.32-1.2.11-server
```

where `<root_temporary_password>` is a random alphanumeric string which must be used to log in to the database for the first time.
In order to change the password, the user should open the app [terminal interface](../guide/submitting.md#job-running) and access the database with the command:

```console
$ mysql -u root -p
```

``` {tip}
Enter password:
```

The login administrator password `<root_temporary_password>` must be copied from the output logs, as in the example above, and pasted in the terminal.
Once inside the MySQL console, a new password should be created with the command:

```sql
mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY 'NewPassword';
```

``` {tip}
Query OK, 0 rows affected (0.20 sec)
```

This password will be used to access the database next time the server is deployed.

``` {note}
A custom root password can also be assigned before submitting the job using the parameter *Admin password*. In this case it is not necessary to reset the password after the first log in.
```

## Connect to the server

As discussed above, the user can access the MySQL console directly from the app terminal interface. However, it is also possible to connect to the server using an external client application. In this case, one has to grant remote access to the database user, e.g., using the following commands from the MySQL console:

```sql
mysql> UPDATE mysql.user SET host='%' WHERE user='root';
```

``` {tip}
Query OK, 0 rows affected (0.00 sec)
<br>
Rows matched: 1  Changed: 0  Warnings: 0
```

and

```sql
mysql> FLUSH PRIVILEGES;
```

``` {tip}
Query OK, 0 rows affected (0.36 sec)
```

In this example the database user coincides with the server administrator. Connections from _any_ external host are allowed. In order to restrict access to the server from _only_ one specific host, it is necessary to replace the `%` in the command above with the corresponding host IP address.

On the one hand, if the client application runs within another interactive app available on UCloud, one can connect directly to the MySQL server, as outlined [here](./general_settings.md#connect-to-other-jobs). In this case the server *hostname* is configured as an external parameter via the option *Connect to other jobs*.

On the other hand, if the MySQL client is a third-party application, which is not deployed on UCloud, it is necessary to assign a [static IP address](./general_settings.md#attach-public-ip-addresses) to the server, using the corresponding option *Public IP*.

``` {note}
By default remote access to the MySQL server is established over the TCP port ``3306``. The same port should be open on the network firewall of the public IP address.
```

## Use option files

A customized server configuration can be specified using the parameter *Option file*. An example is shown below:

```ini
[client]
port=3306

[mysqld]
port=3306
key_buffer_size=16M
max_allowed_packet=128M
bind-address=0.0.0.0

[mysqld-8.0]
sql_mode=TRADITIONAL
```

To check the global configuration variables from the MySQL console, use the commands:

```sql
mysql> SELECT @@GLOBAL.innodb_data_file_path;
```

``` {tip}
+--------------------------------+
<br>
| @@GLOBAL.innodb_data_file_path |
<br>
+--------------------------------+
<br>
| ibdata1:12M:autoextend &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
<br>
+--------------------------------+
<br>
1 row in set (0.00 sec)
```

and

```sql
mysql> SHOW VARIABLES;
```

For more information about option files, check the official documentation [here](https://dev.mysql.com/doc/refman/8.0/en/option-files.html).
