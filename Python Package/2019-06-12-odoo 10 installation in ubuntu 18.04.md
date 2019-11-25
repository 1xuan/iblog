# odoo 10 installation in ubuntu 18.04

[TOC]

### get source code

- Download source code from [ http://nightly.odoo.com/10.0/nightly/src/odoo_10.0.latest.tar.gz]( http://nightly.odoo.com/10.0/nightly/src/odoo_10.0.latest.tar.gz)

- unpackage: `tar -zxvf odoo_10.0.latest.tar.gz`

- make directory for odoo and move:

  ```shell
  mkdir /opt/odoo/
  mv odoo-10.0 /opt/odoo/
  ```

### database

-  install postgresql

  ```shell
  sudo apt-get install postgresql
  ```

- create database user (note: you can create a user that name is same as current linux user, or another. And, if you create same name user, you can run odoo in current environment and don't need to change user. Another key point, when you run odoo and you never create user, then set configure file the parameter db_user=False and db_password=False Finally,  it will create database by current linux user. For last statement, I'm not sure.)

  ```shell
  # cerate current linux user
  sudo su - postgres -c "createuser -s yixuan"
  
  # OR create another user
  sudo -u postgres createuser --createdb --no-createrole --no-superuser --pwprompt odoo
  ```

### python package installation

```shell
sudo apt-get install libxml2 libxslt-dev libpq-dev libldap2-dev libsasl2-dev
sudo apt-get install python-pip
sudo pip install -r /opt/odoo/odoo-10/requirements.txt
```

### install basic dependencies

```shell
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install npm nodejs node-less
sudo npm install -g less less-plugin-clean-cs

# ubuntu 18.04 have wkhtmltopdf already, otherwise install it manually
sudo apt-get install wkhtmltopdf
```

### set odoo config file

-  You can make it `odoo.conf` anywhere

  ```
  [options]
  
  ; This is the password that allows database operations:
   
  ; admin_passwd = admin
   
  db_host = 127.0.0.1
   
  db_port = 5432
   
  db_user = Your_db_user_name
   
  db_password = Your_db_password
   
  log_level = warn
   
  addons_path =/opt/odoo/odoo-10.0/odoo/addons
   
  ;workers = 2
  ```

### done

```shell
./odoo-bin		# run after login created user for database

# OR add some parameter
# use the -s option to create the default configuration file and store the current instance configuration into it,
-d practice --addons-path="/home/yixuan/PycharmProjects/custom-addons, odoo/addons" -s 	
```



## reference

[Ubuntu18.04 安装 Odoo10](http://www.pianshen.com/article/8233354039/)

[Installing Odoo](https://www.odoo.com/documentation/10.0/setup/install.html)

*<<Odoo 10 Development Essentials>> P9-P13*


### some trouble in the way

- lock of dependencies

    *solution*: 
    
    ~~~shell
    Step 1: Add PostgreSQL Apt Repository
    
    $ sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
    $ wget -q https://www.postgresql.org/media/keys/ACCC4CF8.asc -O - | sudo apt-key add -

    Step 2: Install PostgreSQL

    $ sudo apt-get update
    $ sudo apt-get upgrade

    $ sudo apt-get install postgresql postgresql-contrib libpq-dev pgadmin3

    Step 3: Connecting to PostgreSQL

    $ sudo su - postgres
    $ psql

    To list the databases type following command

    postgres-# \l
    ~~~
- auth_senderror ... no password

    *solution*:
    
    ~~~shell
    /etc/postgresql/9.3/main/pg_hba.conf

    And Underneath Change '???' to md5:

    local   all             postgres               probably 'peer'

    To:

    local   all             postgres                                md5

    (all change to `trust`)

    sudo /etc/init.d/postgresql reload
    ~~~


