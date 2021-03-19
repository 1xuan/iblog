**解压安装包错误**

当打开装包内文件时，出现`extracting error`的错误，用命令行解压时出现

	unsupported compression method 99
	
这里显示旧的方式不支持这种解压方式，这里采用了AES加密，我们可以安装工具来解决

	sudo apt install p7zip-full
	
然后通过下面的命令来解压

	7z x file.zip
更多可以参考[ZIP unsupported compression method 99](http://juljas.net/lpt/post/zip-compression-method-99) 


**将raspbian烤录格式化移动硬盘**

	sudo fdisk -l
	sudo dd if=2017-11-29-raspbian-stretch.img of=/dev/sdb1 #if=镜像文件 ， of=硬盘名称

后pc不能识别出sd卡，第二次

	$sudo fdisk -l
	Disk /dev/sdb: 7.5 GiB, 7990149120 bytes, 15605760 sectors
	Units: sectors of 1 * 512 = 512 bytes
	Sector size (logical/physical): 512 bytes / 512 bytes
	I/O size (minimum/optimal): 512 bytes / 512 bytes
	Disklabel type: dos
	Disk identifier: 0x5df5709a
	
	Device     Boot Start      End  Sectors  Size Id Type
	/dev/sdb1        8192    93236    85045 41.5M  c W95 FAT32 (LBA)	
	
此时用命令

	sudo dd bs=1M if=2017-11-29-raspbian-stretch.img of=/dev/sdb # 用DISC盘符而不是Device盘符
	
**启动树莓派之后打开ssh连接（这里需要用到显示器）**

**ubuntu通过ssh连接树莓派**

- 然后网线连接电脑和树莓派
- 设置连接中的ipv4为共享设置
- 安装nmap和openssh-client

		sudo apt-get install nmap
		sudo apt-get install openssh-client
	
- 查看连接信息找到ip地址10.42.0.1, 找到树莓派ip

		$nmap 10.42.0/24
		
		Nmap scan report for 10.42.0.61
		Host is up (0.0045s latency).
		Not shown: 999 closed ports
		PORT   STATE SERVICE
		22/tcp open  ssh
		
- 连接树莓派， 输入密码

		ssh pi@10.42.0.61
		

		
		
		



	

	