from APP import Web
import selenium

username = '1111'
password = ''


modification_number = ['M201801041204','M201801050698','M201801050030']

if __name__ == '__main__':

    try:
        Web.getTS(username,password)
    except selenium.common.exceptions.NoSuchElementException:
        print(111111)


