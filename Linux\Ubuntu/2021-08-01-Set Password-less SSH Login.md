## In Local Host

- generate rsa key

~~~bash
$ ssh-keygen
... # omit
~~~

- copy the public key to remote-host

~~~bash
$ ssh-copy-id -i ~/.ssh/id_rsa.pub remote-host
~~~

- final

~~~bash
$ ssh user@remost_host
Welcome to Ubuntu 18.04.5 LTS (GNU/Linux 4.15.0-117-generic x86_64)
... # omit
~~~


**reference**

[3 Steps to Perform SSH Login Without Password Using ssh-keygen & ssh-copy-id](https://www.thegeekstuff.com/2008/11/3-steps-to-perform-ssh-login-without-password-using-ssh-keygen-ssh-copy-id/)
