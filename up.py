from ftplib import FTP
import os

host = 'office.ai4health.com'
port = 8021
username = 'zjjm'
password = 'ftp_123_zjjm'


def ftpconnect(host, port, username, password):
    ftp = FTP()
    # ftp.set_debuglevel(2)
    ftp.connect(host, port)
    ftp.login(username, password)
    return ftp


def downloadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'wb')
    ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize)
    ftp.set_debuglevel(0)
    fp.close()


def uploadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'rb')
    ftp.storbinary('STOR ' + remotepath, fp, bufsize)
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
