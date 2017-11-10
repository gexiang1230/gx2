#coding:utf-8
import paramiko,time
import Crypto
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh.connect('39.106.14.117',22,'root','qwe123!@#QWE')
dirName='linuxTest'
stdin,stdout,stderr=ssh.exec_command('ls')
dircontent = stdout.read().decode()

if dirName in dircontent.splitlines():
    print'{}已经存在'.format(dirName)
else:
    print'make dir{}'.format(dirName)
    ssh.exec_command("mkdir {}".format(dirName))
#传输文件
ftp=ssh.open_sftp()
ftp.put('memory.py', '{}/memory.py'.format(dirName))
# 检查文件是否传输成功，可以将检查文件是否存在机器，做成一个函数。。。


# 执行脚本


# 考虑到长时间没有消息，网络连接可能会被断开。 到网上搜索一番后。
# 设置一个保持连接的参数
transport = ssh.get_transport()
transport.set_keepalive(30)

print('remote exec python memory.py')
ssh.exec_command("cd %s; python memory.py" % dirName)

print('wait for 30 seconds...')
time.sleep(30)


# 传输文件
sftp = ssh.open_sftp()
sftp.get('{}/ret.txt'.format(dirName),'ret.txt')
sftp.close()

ssh.close()

