from APP import Web,Ftp
from config import web,cFtp

w_username = web.TSusername
w_password = web.TSpassword

f_username = cFtp.ftp_username
f_password = cFtp.ftp_password

ip = cFtp.ftp_ip
port = cFtp.ftp_port
config_url = cFtp.ftp_url

url1 = r


modification_number = 'M201712210622'

if __name__ == '__main__':
    Web.getTS(w_username,w_password)
    a = Web.query(modification_number)
    webget_url = a

    Ftp.download(ip,port,f_username,f_password,config_url,webget_url)


