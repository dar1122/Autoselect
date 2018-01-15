#-*- coding:utf-8 -*-
from config import cFtp
from APP import Ftp

username = cFtp.ftp_username
password = cFtp.ftp_password
ip = cFtp.ftp_ip
port = cFtp.ftp_port
config_url = '1111'
webget_url = "/规范化递交/M201712280073-产品日终/"
gopath = '///'



if __name__ == '__main__':
    Ftp.download(ip,port,username,password,config_url,webget_url,gopath)