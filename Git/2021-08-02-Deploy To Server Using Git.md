## In Server End

- init a bare repo

~~~bash
$ git init --bare repo.git
~~~

- add hooks `post-receive`

~~~bash
$ vim repo.git/hooks/post-receive
~~~

**add following content**

*file repo.git/hooks/post-receive*

~~~
#!/bin/bash
git --work-tree=/root/repo --git-dir=/root/repo.git checkout -f

cd /root/repo

# execute whatever you want to do. It's a demo
cat README.md
~~~

**note: it should create /root/repo manually**

- make the file executable

~~~bash
$ chmod +x repo.git/hooks/post-receive
~~~

## In Client End 

- git clone

~~~bash
$ git clone root@{YOUR_SERVER}:/root/repo.git
~~~

- add remote repo in server

~~~bash
$ git remote add origin root@${YOUR_SERVER}:/root/repo.git
~~~

- push changes to remote

~~~bash
$ git push origin master
~~~

**reference**

[Video: Deploy to Your Server Using Git](https://www.youtube.com/watch?v=H6UU7TsyrGs)

