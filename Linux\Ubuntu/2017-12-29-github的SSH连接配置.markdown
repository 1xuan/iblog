---
layout: post
title: ubuntu下利用git向github提交项目
date: 2017-12-29 20:32
---

### 安装git

	apt-get install libcurl4-gnutls-dev libexpat1-dev gettext libz-dev libssl-dev                          #安装依赖
	sudo apt-get install git
	# 老版本中git的名字是git-core
	git --version                       #查看git版本
	
### 配置git

	ssh-keygen -t rsa -C "your_email@youremail.com"     #本地创建ssh key
(SSH是一种网络协议，用于计算机之间的加密登录。目前是每一台 Linux 电脑的标准配置。而大多数 Git 服务器都会选择使用 SSH 公钥来进行授权，所以想要在 GitHub 提交代码的第一步就是要先添加 SSH key 配置。)

之后会要求确认路径和输入密码，我们这使用默认的一路回车就行。成功的话会在~/下生成.ssh文件夹，进去，打开id_rsa.pub，复制里面的key。

	cat ~/.ssh/id_rsa.pub                                        #查看公钥

回到github上，进入 Account Settings（账户配置），左边选择SSH Keys，Add SSH Key,title随便填，粘贴在你电脑上生成的key。

	$ ssh -T git@github.com                                     #验证是否成功
	You ve successfully authenticated, but GitHub does not provide shell access      #表示成功连上github
	#可能会出现下面的错误
	sign_and_send_pubkey: signing failed: agent refused operation Permission denied (publickey).
	$ ssh-add                                           #执行这条命令,然后在执行上一条命令,可能需要在.ssh目录下执行
	
	
### 更多情况

#### 参照
[从0开始学习 GitHub 系列之「向GitHub 提交代码」](http://stormzhang.com/github/2016/06/04/learn-github-from-zero4/)  
[Github 简明教程](http://www.runoob.com/w3cnote/git-guide.html) 

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

	
