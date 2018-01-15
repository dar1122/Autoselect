from APP import Web,Ftp,Rar,Move
from config import cFtp
import threading

w_username = web.TSusername
w_password = web.TSpassword

f_username = cFtp.ftp_username
f_password = cFtp.ftp_password

ip = cFtp.ftp_ip
port = cFtp.ftp_port
config_url = cFtp.ftp_url

url1 = rar1.rar_url

modification_number = ['M201801050698,M201801050030,M201801041204']

updata_mumbers = ['his_dbksett_or.sql    V8.0.8.67,user_Secu_TablePatch.sql    V8.0.8.115,libs_as_ftsecusettflow.10.so    V8.0.8.55,c_secusett.dll    V8.0.8.574']












if __name__ == '__main__':

    Web.getTS(w_username,w_password)

    for num in modification_number:



        requir_list = []
        a = Web.query(num)
        info1=Web.updateinfo()
        Web.mod_del()

        name_list = Move.sp_tan(info1)
        for member in name_list:
            for updata_member in updata_mumbers:
                if member==updata_member:
                    new_member = member.split()
                    del new_member[1]
                    requir_list.extend(new_member)

        to_updata_list = requir_list

        webget_url = a

        url2 = Ftp.download(ip,port,f_username,f_password,config_url,webget_url)
        Rar.rarto(url1,url2,to_updata_list)

