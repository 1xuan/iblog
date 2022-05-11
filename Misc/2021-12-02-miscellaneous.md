# DB
- There are 600k records in device\_log without index; (I am not aware of the IO rate of disk)

~~~sql
select * from device_log;
~~~
comsumed time: 5.9s (So the rate is roughly: 100k/s)

~~~sql
select count(*) from device_log;
~~~~
time: 350ms

~~~sql
select * from device_log offset 0 limit 10000;
~~~
time: 109ms (The time will vary slightly as offset changes)


# file

There are 175k rows in a log file;

- The total size is 11 M
- So the ratio is roughly `16k/M

