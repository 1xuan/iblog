## Allow remote access

- Modify file `/etc/postgresql/10/main/postgresql.conf`

~~~
#listen_addresses = 'localhost'
~~~

to 

~~~
listen_addresses = '*'
~~~

- Modify file `/etc/postgresql/10/main/pg_hba.conf`

~~~
# IPv4 local connections:
host    all             all             127.0.0.1/32            md5
~~~

to 

~~~
# IPv4 local connections:
host    all             all             0.0.0.0/0            md5
~~~
