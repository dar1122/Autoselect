from APP import Web,Ftp,Rar
from config import web,cFtp,rar1

w_username = web.TSusername
w_password = web.TSpassword

f_username = cFtp.ftp_username
f_password = cFtp.ftp_password

ip = cFtp.ftp_ip
port = cFtp.ftp_port
config_url = cFtp.ftp_url

url1 = rar1.rar_url

modification_number = 'M201712210622'

if __name__ == '__main__':
    Web.getTS(w_username,w_password)
    a = Web.query(modification_number)
    webget_url = a

    url2 = Ftp.download(ip,port,f_username,f_password,config_url,webget_url)
    Rar.rarto(url1,url2)

