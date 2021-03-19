### locale.Error: unsupported locale setting

在ubuntu下安装好pip3后：

	$ pip3 install virtualenv
	Traceback (most recent call last):
  	File "/usr/bin/pip3", line 11, in <module>
    	sys.exit(main())
  	File "/usr/lib/python3/dist-packages/pip/__init__.py", line 215, in main
    	locale.setlocale(locale.LC_ALL, '')
  	File "/usr/lib/python3.5/locale.py", line 594, in setlocale
    	return _setlocale(category, locale)
	locale.Error: unsupported locale setting

出现上面的错误，我unbuntu下python2和3是同时存在的， pip2是自带的，pip2安装是没有问题的（并且pip3和pip2的安装路径是有一点区别，我不知道跟这个有没有关系）

	$ pip3 --version
	pip 8.1.1 from /usr/lib/python3/dist-packages (python 3.5)
	$ pip --version
	pip 9.0.1 from /usr/local/lib/python2.7/dist-packages (python 2.7)

然后网上找到解决办法：

	$ locale -a
	C
	C.UTF-8
	en_AG
	en_AG.utf8
	en_AU.utf8
	en_BW.utf8
	en_CA.utf8
	en_DK.utf8
	en_GB.utf8
	en_HK.utf8
	en_IE.utf8
	en_IN
	en_IN.utf8
	en_NG
	en_NG.utf8
	en_NZ.utf8
	en_PH.utf8
	en_SG.utf8
	en_US.utf8
	en_ZA.utf8
	en_ZM
	en_ZM.utf8
	en_ZW.utf8
	POSIX
	
	$ export LC_ALL=C
	
至于这个有什么用可以参考[当LC_ALL等于C以后](https://blog.csdn.net/spring1208/article/details/54913461)

最后这个问题算是顺利解决了。。。

### Command "python setup.py egg_info" failed with error code 1

当创建好`virtualenv`环境后，pip安装到某一个包时：

	$ pip install django-pure-pagination
	Collecting django-pure-pagination
	  Using cached https://files.pythonhosted.org/packages/55/43/50c475f408d3350cec340855970a5ce02ea12f5a53d520315f200b4847a1/django-pure-pagination-0.3.0.tar.gz
	    Complete output from command python setup.py egg_info:
	    Traceback (most recent call last):
	      File "<string>", line 1, in <module>
	      File "/tmp/pip-install-9pzg_3l8/django-pure-pagination/setup.py", line 5, in <module>
		README = readme.read()
	      File "/home/yixuan/sites/yixuan.fun/env/lib/python3.5/encodings/ascii.py", line 26, in decode
		return codecs.ascii_decode(input, self.errors)[0]
	    UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3 in position 672: ordinal not in range(128)
	    
	    ----------------------------------------
	Command "python setup.py egg_info" failed with error code 1 in /tmp/pip-install-9pzg_3l8/django-pure-pagination/
	
又出现了上面的错误，顺着`Command "python setup.py egg_info" failed with error code 1`又找到很多解决方法，但是这里能看到`UnicodeDecodeError: 'ascii' codec can't decode byte`这个错误是跟编码有关的。

于是这里修改系统的默认编码：

	$ locale
	LANG=en_US.UTF-8
	LANGUAGE=
	LC_CTYPE="C"
	LC_NUMERIC="C"
	LC_TIME="C"
	LC_COLLATE="C"
	LC_MONETARY="C"
	LC_MESSAGES="C"
	LC_PAPER="C"
	LC_NAME="C"
	LC_ADDRESS="C"
	LC_TELEPHONE="C"
	LC_MEASUREMENT="C"
	LC_IDENTIFICATION="C"
	LC_ALL=C

	$ export LC_ALL=en_US.UTF-8
	# 可以看到这里的系统编码全都修改了
	$ locale 
	LANG=en_US.UTF-8
	LANGUAGE=
	LC_CTYPE="en_US.UTF-8"
	LC_NUMERIC="en_US.UTF-8"
	LC_TIME="en_US.UTF-8"
	LC_COLLATE="en_US.UTF-8"
	LC_MONETARY="en_US.UTF-8"
	LC_MESSAGES="en_US.UTF-8"
	LC_PAPER="en_US.UTF-8"
	LC_NAME="en_US.UTF-8"
	LC_ADDRESS="en_US.UTF-8"
	LC_TELEPHONE="en_US.UTF-8"
	LC_MEASUREMENT="en_US.UTF-8"
	LC_IDENTIFICATION="en_US.UTF-8"
	LC_ALL=en_US.UTF-8

最后顺利安装好库文件。

**注意**

`export`跟改，系统重启后，环境会会还原为之前的情况。

具体可参考[Ubuntu修改系统默认编码](https://blog.csdn.net/example440982/article/details/71218685)

**原因**

再次重装系统后重复此过程中，在执行完`apt-get upgrade`时弹出一个窗口，我记不太清楚第一行有什么`... maintain’s ...`， 第二行是什么`keep local ...`,这次我没有像上次一样选择第二行， 而是选择了第一行。再执行上面的命令时再没有遇见上面的任何错误。

