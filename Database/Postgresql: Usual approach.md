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

