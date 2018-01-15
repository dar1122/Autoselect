# coding = utf-8
import string
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import time,re

from selenium.webdriver.common.keys import Keys


def getTS(username,password):
    global driver
    driver = webdriver.PhantomJS("E:/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe")
    driver.get("https://ts.hundsun.com/")
    #输入用户名和密码
    time.sleep(3)
    driver.find_element_by_id('username').send_keys(username)
    driver.find_element_by_id('password').send_keys(password)
    time.sleep(2)
    #登录
    driver.find_element_by_xpath('//*[@id="bottom"]/input[4]').click()
    time.sleep(5)


    # 进入修改单界面
    driver.find_element_by_xpath('//*[@id="button-1018-btnInnerEl"]').click()
    time.sleep(3)

    #选择auto模板

#    driver.find_element_by_id('lovcombo-2574-inputEl').send_keys('auto')
#    driver.find_element_by_id('lovcombo-2574-inputEl').send_keys(Keys.ENTER)
    time.sleep(5)
    print('登陆成功')



def query(modification_number):
    #输入修改单编号
    driver.find_element_by_name('modifyNum').send_keys(modification_number)
    driver.find_element_by_link_text('查 询').click()
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source,'html')
    #获取输出路径
    darid = re.compile('/[\u4e00-\u9fa5]+/[A-Z]*[0-9]+-[\u4e00-\u9fa5]+/')
    list = soup.find("div",{"data-qtip":darid}).text
    output_url = list
    return output_url

#查询升级文件名称
def updateinfo():
    soup1 = BeautifulSoup(driver.page_source,'html')
    divid = re.compile('.+<br>')
    info = soup1.find("div",{"data-qtip":divid}).text
    return info

def mod_del():
    driver.find_element_by_name('modifyNum').clear()


