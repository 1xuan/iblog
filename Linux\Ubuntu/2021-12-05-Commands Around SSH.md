## Password-Less login

### execute linux command on remote host over ssh

- executing command on remote host over ssh

~~~bash
ssh {remote_host} 'ls /home'
~~~

- executing multiple commands

~~~bash
ssh {remote_host} < commands.txt
~~~

- executing arbitrary screen-based program on remote host

~~~bash
ssh -t {remote_host} vim demo.txt
~~~



### port forwarding

- ssh

**localhost port forwarding**

~~~bash
ssh -L 123:localhost:456 remotehost
~~~

**remote port forwarding**

~~~bash
ssh -R 123:localhost:456 remotehost
~~~

### mount remote directory on localhost

- sshfs

~~~bash
sudo sshfs -o allow_other,default_permissions,IdentityFile=/home/yixuan/.ssh/id_rsa root@REMOTE_HOST:/root /mnt/myserver
~~~

### add ssh key

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

