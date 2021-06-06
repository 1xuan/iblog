## datetime Module

### datetime class

~~~python
>>> from datetime import datetime

# get time or now
>>> datetime.now()
datetime.datetime(2021, 5, 3, 1, 8, 58, 229439)

# convert timestamp to datetime
>>> import time
>>> datetime.fromtimestamp(time.time())
datetime.datetime(2021, 5, 3, 19, 7, 38, 49466)

# specify datetime
>>> datetime(year=2021, month=5, day=3)
datetime.datetime(2021, 5, 3, 0, 0)

# convert time from datetime object to string
>>> datetime.now().strftime('%Y:%m:%d %H:%M:%S.%f')
'2021:05:03 01:34:14.633496'

# convert time from string to datetime object
>>> datetime.strptime('2021:05:03 01:34:14.633496', '%Y:%m:%d %H:%M:%S.%f')
datetime.datetime(2021, 5, 3, 1, 34, 14, 633496)

# return the datetime formatted according to ISO
>>> datetime.now().isoformat()
'2021-05-03T01:40:16.169805'

# compute the date
from datetime import timedelta
>>> datetime.now() + timedelta(days=1)
datetime.datetime(2021, 5, 4, 18, 57, 38, 818388)

~~~

### data

~~~python
# get date of today
>>> from datetime import date
>>> date.today()
datetime.date(2021, 5, 3)

# get date from timestamp
import time
>>> date.fromtimestamp(time.time())
datetime.date(2021, 5, 3)

# repalce year temporarily
>>> d = date.today()
>>> d.replace(year=2222)
datetime.date(2222, 5, 3)

~~~

### time

~~~python
from datetime import time

>>> t = time(1, 2, 3)
datetime.time(1, 2, 3)
>>> str(time(1, 2, 3))
'01:02:03'

>>> time.max
datetime.time(23, 59, 59, 999999)
~~~

## time Module

~~~python
import time
>>> time.strftime('%Y-%m-%d')
'2021-05-03'

~~~

## calendar Module

~~~python
import calendar

>>> calendar.monthrange(2021, 5)
(5, 31)     # (the weekday of first day, the number of days)

~~~

**Reference**

- [PyMOTW-3: datetime — Date and Time Value Manipulation](https://pymotw.com/3/datetime/index.html)

