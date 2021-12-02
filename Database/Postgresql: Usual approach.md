#### dump data into or out of table

~~~sql
COPY table TO '/tmp/table.csv' DELIMITER ',';
COPY table FROM '/tmp/table.csv' DELIMITER ',';
~~~

#### move data from one table to another

- move data to an exist table

~~~sql
with moved_rows as (
    delete from <original_table>
    returning *
)
insert into <existing_table> select * from moved_rows;
~~~

- move data to a new table

~~~sql
create table <new_table> as
with moved_rows as (
    delete from <original_table>
    returning *
)
select * from moved_rows;
~~~


# PG COMMAND

- next query result be export to file
~~~sql
\o ./result_file ()
~~~

- back up pg

~~~bash
$ pg_dump -C -h {TARGET_HOST} -p 5432 -U postgres {OLDDB} | psql -h localhost -p 5432 -U postgres -d {NEWDB}
~~~

