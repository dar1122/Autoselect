from APP import Web
from config import web

username = web.TSusername
password = web.TSpassword


modification_number = 'M201712280073'

if __name__ == '__main__':
    Web.getTS(username,password)
    a = Web.query(modification_number)
    print(a)

