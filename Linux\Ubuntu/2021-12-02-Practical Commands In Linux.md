# FILE

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
$ xxd FILE    # convert binary to text
$ xxd -r FILE    # convert text to binary
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

## scanning ports

- check host port connection
~~~bash
$ nc -zv 139.196.104.13 1883
~~~

- faster scan for all ports
~~~bash
$ nmap  -p0-65535 192.168.122.1 -T5
~~~

- Scan All TCP Ports
~~~bash
$ nmap -p- 192.168.122.1
~~~

## capturing tcp traffic

- tcpdump
~~~bash
$ sudo tcpdump -i any -w /tmp/http.log &
~~~

