from APP import Web
from config import web

username = web.TSusername
password = web.TSpassword


modification_number = ['M201801041204','M201801050698','M201801050030']

if __name__ == '__main__':
    Web.getTS(username,password)
    for num in modification_number:
        a=Web.query(num)
        print(a)
        Web.updateinfo()
        Web.mod_del()

