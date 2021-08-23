from ftplib import FTP
import os

host = 'office.ai4health.com'
port = 8021
username = 'zjjm'
password = 'ftp_123_zjjm'


# 连接并登录
def ftpconnect(host, port, username, password):
    ftp = FTP()
    # ftp.set_debuglevel(2)         #打开调试级别2，显示详细信息
    ftp.connect(host, port)  # 连接
    ftp.login(username, password)  # 登录，如果匿名登录则用空串代替即可
    return ftp


# 下载文件
def downloadfile(ftp, remotepath, localpath):  # remotepath：上传服务器路径；localpath：本地路径；
    bufsize = 1024  # 设置缓冲块大小
    fp = open(localpath, 'wb')  # 以写模式在本地打开文件
    ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize)  # 接收服务器上文件并写入本地文件
    ftp.set_debuglevel(0)  # 关闭调试
    fp.close()  # 关闭文件


# 上传文件
def uploadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'rb')
    ftp.storbinary('STOR ' + remotepath, fp, bufsize)  # 上传文件
    ftp.set_debuglevel(0)
    fp.close()


if __name__ == "__main__":
    ftp = ftpconnect(host, port, username, password)

    for root, dirs, files in os.walk('./'):
        for file1 in files:
            file_name = os.path.join(root, file1)
            print(file_name)
            uploadfile(ftp, os.path.join("/qwj/arburg/test", file_name[2:]), file_name)

    ftp.quit()
