# FILE

## statistics

### statistics lines of files under directory

- statistics lines of code of project

~~~bash
$ find . -type f -name '*.py' | xargs strings | wc -l
~~~

## view file

- strings (view printable strings in file)

~~~bash
$ strings {BINARYFILE}
~~~

- wc (count lines of file)

~~~bash
$ wc -l {FILE}
~~~

## find files

- find 

~~~bash
$ find -name {FILENAME}
~~~~

- locate (by database)

~~~bash
$ locate one_python_file.py
~~~

more info:

[How to Find Files on Linux with Find and Locate](https://www.servermania.com/kb/articles/how-to-find-files-on-linux-with-find-and-locate/)

## View binary

- xxd
convert binary to text or vice versa
~~~bash
$ xxd FILE    # convert text to binary
$ xxd -r FILE    # convert binary to text
~~~

### find plain-text that match regex through files

- grep

~~~bash
$ grep {WORD} -r ./
~~~
















# NETWORK

- launch a local tcp server
~~~bash
$ nc -l 8000 
~~~

- transport file
~~~
# server:
$ nc -l -p xxx > file2

# sender:
$ nc x.x.x.x xxx < file1
~~~

## for ports

- check host port connection
~~~bash
$ nc -zv 139.196.104.13 1883
~~~

- scan ports
~~~bash
# faster scan for all ports
$ nmap  -p0-65535 192.168.122.1 -T5

# Scan All TCP Ports
$ nmap -p- 192.168.122.1

# scan specific port
$ nmap -p 80 x.x.x.x
~~~

- show connections and timer
~~~
$ ss -tanpo
~~~


## capturing tcp traffic

- tcpdump
~~~bash
$ sudo tcpdump -i any -w /tmp/http.log &
~~~


# Process

## get pid

- get pid by port

~~~
sudo ss -lptn 'sport = :80'
sudo lsof -n -i :80
~~~


# Bash

- redirect stderr to stdout
~~~
$ fuser -v -m ~/.bashrc 2>&1 | wc -l
~~~



