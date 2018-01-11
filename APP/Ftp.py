#-*- coding:utf-8 -*-
import chardet

from ftplib import FTP
import re



def download(ip,port,username,password,config_url,webget_url,go_path):
    ftp = FTP()
    ftp.set_debuglevel(2)
    ftp.connect(ip,port)
    ftp.login(username,password)

    url = config_url+webget_url
    newurl = url.encode("UTF-8").decode("latin-1")
    path = go_path

    ftp.cwd(newurl)
    bufsize = 1024
    lists = ftp.nlst()

    i=0
    for filename in lists:
        s = re.match('.*M[0-9]+-.+-[0-9]+-V[0-9]+.rar',filename)
        if s!=None:
            i+=1
    x=0
    for filename in lists:
        s = re.match('.*M[0-9]+-.+-[0-9]+-V[0-9]+.rar',filename)
        x+=1
        if s!=None:
            if x ==i:
                file_handle = open(path+filename,"wb").write
                ftp.retrbinary("RETR "+filename,file_handle,bufsize)
                w = filename
    ftp.set_debuglevel(0)
    ftp.quit()
    return w

