# Querybook

:::: {tab-set}

::: {tab-item} 3.14.2

[![querybook](badges/release-3.14.2-blue.svg)](https://cloud.sdu.dk/app/jobs/create?app=querybook&version=3.14.2)
![type](badges/type-interactive-yellow.svg)
![access](badges/access-open-green.svg)
* **Operating System:** ![](./badges/Debian-11.5-lightseagreen.svg)
* **Terminal:** ![](./badges/tini-0.19.0-lightseagreen.svg) ![](./badges/tmux-3.1c-lightseagreen.svg)
* **Shell:** ![](./badges/bash-5.1.4-lightseagreen.svg) ![](./badges/fish-3.1.2-lightseagreen.svg) ![](./badges/zsh-5.8-lightseagreen.svg)
* **Editor:** ![](./badges/emacs-27.1-lightseagreen.svg) ![](./badges/nano-5.4-lightseagreen.svg) ![](./badges/vim-8.2-lightseagreen.svg)
* **Package Manager:** ![](./badges/apt-2.2.4-lightseagreen.svg) ![](./badges/dpkg-1.20.12-lightseagreen.svg) ![](./badges/npm-8.5.0-lightseagreen.svg) ![](./badges/pip-23.0.1-lightseagreen.svg)
* **Programming Language:** ![](./badges/GCC-10.2.1-lightseagreen.svg) ![](./badges/Python-3.9.15-lightseagreen.svg) ![](./badges/Python-2.7.18-lightseagreen.svg)
* **Database:** ![](./badges/Elasticsearch-7.17.9-lightseagreen.svg) ![](./badges/PostgreSQL-15.2-lightseagreen.svg) ![](./badges/Redis-6.0.16-lightseagreen.svg)

:::

::: {tab-item} 3.11.1

[![querybook](badges/release-3.11.1-blue.svg)](https://cloud.sdu.dk/app/jobs/create?app=querybook&version=3.11.1)
![type](badges/type-interactive-yellow.svg)
![access](badges/access-open-green.svg)
* **Operating System:** ![](./badges/Debian-11-lightseagreen.svg)
* **Terminal:** ![](./badges/tmux-3.1c-lightseagreen.svg)
* **Shell:** ![](./badges/bash-5.1.4-lightseagreen.svg)
* **Editor:** ![](./badges/emacs-27.1-lightseagreen.svg) ![](./badges/nano-5.4-lightseagreen.svg) ![](./badges/vim-8.2-lightseagreen.svg)
* **Package Manager:** ![](./badges/apt-2.2.4-lightseagreen.svg) ![](./badges/dpkg-1.20.12-lightseagreen.svg) ![](./badges/pip-22.0.4-lightseagreen.svg)
* **Programming Language:** ![](./badges/GCC-10.2.1-lightseagreen.svg) ![](./badges/Python-3.9.14-lightseagreen.svg)
* **Database:** ![](./badges/Elasticsearch-7.13.4-lightseagreen.svg) ![](./badges/PostgreSQL-14.5-lightseagreen.svg) ![](./badges/Redis-6.0.16-lightseagreen.svg)

:::

::::

Querybook is an advance big data IDE discovering, creating, and sharing data analyses, queries, and tables via a notebook interface.

For more information, check [here](https://www.querybook.org).

## Start Querybook app

When starting the application on UCloud, one needs to select *Signup* and enter the required information. By default, this user is the app *Administrator*.

Administrators have all possible rights, including granting or revoking rights to other users and editing other users’ notebooks and dashboards. Custom permissions can be created through the Querybook interface.

``` {note}
All users are registered in the server with an email address. However, there is no email server configured in the backend. Therefore, it is not possible to send emails to the users from the app web interface.
```

## Connect to databases

### PostgreSQL database

The application starts a [PostgreSQL](https://www.postgresql.org/) database server.

The PostgreSQL database directory, named `postgresql`, is created by default in `/work`. After job completion, the database is accessible in the `Jobs/Querybook/$JOB_ID` directory on UCloud.

It is also possible to select a pre-existing PostgresSQL database by importing the corresponding directory using the *Existing PostgreSQL database* optional parameter, which also initializes the `$PGDATA_DIR` environment variable. Database name and login credentials must also be specified using the corresponding optional parameters.

By default the PostgreSQL username is *ucloud*, the password is *ucloud*, and the name of the accessible database is also *ucloud*.

To create a new PostgresSQL user and password and/or choose the name for a new PostgreSQL database, one can use the app [terminal interface](../guide/submitting.md#job-running), e.g.:

```console
$  psql -c "create user $user with encrypted password '$pass';"
$  psql -c "grant all privileges on database $postgres_db to $user;"
```

The general form of the PostgresSQL database connection string is:

```postgresql
postgresql+psycopg2://{username}:{password}@0.0.0.0:5432/{database}
```

The following video shows how to connect to the PostgreSQL database from the Querybook interface and associate the database to an environment.

<video width=100% controls>
  <source src="../query-video1.mov" type="video/mp4">
</video>

### Other query engines

Instead of PostgreSQL it is possible to use different [query engines](https://www.querybook.org/docs/setup_guide/connect_to_query_engines/#all-query-engines).

The necessary packages to connect to the chosen database can be installed through the *Initialization* parameter, via a Bash script. Likewise the associated service can be started within the script. In this case it is necessary to specify the SQLAlchemy connection string to the database via the *Connection string* optional parameter (see, e.g., [here](https://docs.sqlalchemy.org/en/13/core/engines.html) for the string format).

## Celery – Distributed Task Queue

Celery is an open source asynchronous task queue system which is based on distributed message passing, focusing on operations in real time.

Celery by default uses multiprocessing to perform concurrent task execution. The number of worker processes/threads can be changed using the *worker concurrency* parameter and, if not set, it defaults to the number of available CPUs.

## uWSGI settings

Several parameters, including the worker class, and the number of workers and threads, can be tuned by modifying the `/opt/querybook/uwsgi.ini` file, see [here](https://uwsgi-docs.readthedocs.io/en/latest/Configuration.html) for details.

In order to use the customized version, the user must copy the new `uwsgi.ini` file in the `/opt/querybook` directory and overwrite the default configuration. This operation can be done with a Bash script through the *Initialization* optional parameter.

## Share and collaborate

Querybook allows users live query collaborations.

The figure below shows an example of how to share a notebook.

<br>

<img src="figs/q-share.png" alt="drawing" width="90%" align="center">

<br>

Collaborators can *sign up* and request edit permissions.

``` {note}
The URL can be shared with collaborators only if the app is deployed with a [public link](general_settings.md#configure-custom-links).
```
