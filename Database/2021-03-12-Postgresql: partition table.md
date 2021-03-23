# Partition Table

- postgresql 10

## Declarative Partition

###  Introduce

Partitioning refers to splitting what is logically one large table into smaller physical pieces.

Partitioning can provide several benefits:

- to improve perfomance, and reduce index size

- bulk loads and deletes can be accomplished by adding or removing partitions.

- seldom-used data can be migrated to cheaper and slower storage media.

The benefits will normally be worthwhile only when a table would otherwise be very large. The exact point at which a table will benefit from partitioning depends on the application, although a rule of thumb is that the size of the table should exceed the physical memory of the database server.

### Limitations

- There is no facility available to create the matching indexes on all partitions automatically. Indexes must be added to each partition in seperate commands.

- Since primary keys are not supported on partitioned tables, foreign keys referencing partitioned tables are not supported.

### They way to create

~~~sql

# create partitioned table
CREATE TABLE device_log (
   device_id       integer,
   datetime        timestamp,
   data            jsonb,
) PARTITION BY RANGE (datetime);

# create table partition
CREATE TABLE partition_device_log_2021
PARTITION OF device_log
FOR VALUES
FROM ('2021-01-01') TO ('2022-01-01')

# insert records
INSERT INTO device_log VALUES (1, '2021-01-01','{}');

# drop partition
DROP TABLE partition_device_log_2021;

# detach partition
ALTER TABLE device_log DETACH PARTITION partition_device_log_2021;

~~~

## Inheritance


**reference**

[5.10. Table Partitioning](https://www.postgresql.org/docs/10/ddl-partitioning.html)

[https://www.enterprisedb.com/blog/postgres-table-partitioning](https://www.enterprisedb.com/blog/postgres-table-partitioning)

[PostgreSQL 10.0 内置分区表](https://developer.aliyun.com/article/66946)

