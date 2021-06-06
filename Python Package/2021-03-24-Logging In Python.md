# Logging In Python

## Simplest Way

~~~Python
import logging

logging.warn("Have Fun")
~~~

output:
~~~shell
WARNING:root:Have Fun
~~~

## logger

### Configure logging

~~~Python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)
logging.info('Have Fun')
~~~

output:
~~~shell
2021-04-02 16:01:19,580 [INFO] Have Fun
~~~

It should be noted that calling basicConfig() to configure the root logger works only if the root logger has not been configured before. **Basically, this function can only be called once.**

## Capturing stack Traces

~~~Python
import logging

try:
  c = 1 / 0
except Exception as e:
  logging.error("Exception occurred", exc_info=True)
~~~

output:
~~~shell
ERROR:root:Exception occurred
Traceback (most recent call last):
  File "exceptions.py", line 6, in <module>
    c = a / b
ZeroDivisionError: division by zero
~~~

## hierarchy

Following [Advanced Logging Tutorial](https://docs.python.org/3.6/howto/logging.html#advanced-logging-tutorial) said:

> Logging is performed by calling methods on instances of the Logger class (hereafter called loggers). Each instance has a name, and they are conceptually arranged in a namespace hierarchy using dots (periods) as separators. For example, a logger named ‘scan’ is the parent of loggers ‘scan.text’, ‘scan.html’ and ‘scan.pdf’. Logger names can be anything you want, and indicate the area of an application in which a logged message originates.
> A good convention to use when naming loggers is to use a module-level logger, in each module which uses logging, named as follows:

~~~Python
logger = logging.getLogger(__name__)
~~~

- propagate

Attribute `propagate` be used to propagate logs in current logger to the parent logger.


## handler

### Specifing Handler

~~~Python
improt logging

logger = logging.getLogger('example_logger')
logger.warning('This is warning')
~~~

It will get by default `root logger` if you don't specify logger name.

### Using Handler

You can custom your logger and redirect logs in handler, and you can set different config for various handlers in one logger separately.

~~~Python
import logging

# Create a custom logger
logger = logging.getLogger(__name__)

# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file.log')
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.warning('This is a warning')
logger.error('This is an error')
~~~

output:
~~~shell
__main__ - WARNING - This is a warning
__main__ - ERROR - This is an error
~~~

## specific problem

### Using rotatingFileHandler to save log

~~~Python
import logging
from logging.handlers import RotatingFileHandler

root_logger = logging.getLogger()
rotating_file_handler = RotatingFileHandler(
    filename='exmaple.log',
    mode='a',
    maxBytes=30 * 1024 * 1024,
    backupCount=1,
)
root_logger.addHandler(rotating_file_handler)
~~~


**reference**

[Logging in Python](https://realpython.com/python-logging/)

