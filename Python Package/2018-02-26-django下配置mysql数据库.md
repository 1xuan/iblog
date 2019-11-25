---
layout: post
title: django下配置 MySQL 数据库
date: 2018-02-26 14:10
---

本文是讲述 django 中 mysql 数据库的配置

	DATABASES = { 
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'xblog',    ## 数据库名称
        'USER': 'root',
        'PASSWORD': 'password',    ## 安装 mysql 数据库时，输入的 root 用户的密码
        'HOST': '127.0.0.1',
    		}
	}
	
（若是你要在 py 文件中作中文注释，不要忘了在文件开头加上#coding:utf-8）

### ubuntu安装mysql

	$ sudo apt-get install mysql-server mysql-client
	#在过程中按照提示输入 mysql root 用户的密码，此密码将用于 settings.py 中
	
	$ mysql -u root -p
	Enter password: ## 输入 mysql root 用户密码，进入数据库
	
	mysql> create database xblog default charset utf8 collate utf8_general_ci;
	Query OK, 1 row affected (0.20 sec)
	
### 安装PyMySQL
 MySQLdb当时可能源太旧不支持python3, 所以我使用pymysql来代替。
	
	$ pip install PyMySQL 
	
在django中setting.py的设置不变，然后在manage.py中添加下列代码：

	import pymysql
	pymysql.install_as_MySQLdb()
	
可以参考[How to config Django using pymysql as driver?  -stackoverflow](https://stackoverflow.com/questions/34777755/how-to-config-django-using-pymysql-as-driver) 
	
	
	
