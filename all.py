# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dar.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from unrar import rarfile
import os
from ftplib import FTP
import re,time
from xlwt import *
from bs4 import BeautifulSoup
from selenium import webdriver
import selenium
import ftplib


class cFtp:
    ftp_ip = ''
    ftp_port = 
    ftp_username = ''
    ftp_password = ''







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

def sp_tan(a):

    b = str.maketrans(' ', ' ', '[')

    x = a.translate(b)

    c = str.maketrans(']', ',')

    new_x = x.translate(c)

    p = new_x.split(',')

    return p

def rarto(url1,url2,getname,to_url):

    file = rarfile.RarFile(url1+url2)

    x=file.namelist()

    for name in x:
        for num in getname:
            if num==name :
                if re.match('.+.so', num) != None:
                    file.extract(num,to_url+'so')
                elif re.match('.+.ini', num) != None:
                    file.extract(num, to_url+'ini')
                elif re.match('.+.dll', num) != None:
                    file.extract(num, to_url+'dll')
                elif re.match('.+.sql', num) != None:
                    file.extract(num, to_url+'sql')
                else:
                    file.extract(num, to_url)

def updata_info(updata_mumbers,get_path):
    ini_list = []
    so_list = []
    dll_list = []
    sql_list = []

    book = Workbook(encoding='utf-8')
    tmp = book.add_sheet('升级文件信息', cell_overwrite_ok=True)
    for every_member in updata_mumbers:

        if re.match('.+.sql.+', every_member) != None:
            sql_list.append(every_member)
        elif re.match('.+.ini.+', every_member) != None:
            ini_list.append(every_member)
        elif re.match('.+.dll.+', every_member) != None:
            dll_list.append(every_member)
        elif re.match('.+.so.+', every_member) != None:
            so_list.append(every_member)

    num1 = len(sql_list)
    num2 = len(ini_list)
    num3 = len(dll_list)
    num4 = len(so_list)

    tmp.write(int(num1 / 2), 0, 'sql文件')
    tmp.write(num1 + 1 + int(num2 / 2), 0, 'ini文件')
    tmp.write(num1 + num2 + 2 + int(num3 / 2), 0, 'dll文件')
    tmp.write(num1 + num2 + num3 + 3 + int(num4 / 2), 0, 'so文件')

    i = 0
    for sql in sql_list:
        tmp.write(i, 2, sql)
        i = i + 1

    i = i + 1
    for ini in ini_list:
        tmp.write(i, 2, ini)
        i = i + 1
    i = i + 1
    for dll in dll_list:
        tmp.write(i, 2, dll)
        i = i + 1
    i = i + 1
    for so in so_list:
        tmp.write(i, 2, so)
        i = i + 1
    book.save('{}升级说明.xls'.format(get_path))

def getTS(username,password):
    global driver
    driver = webdriver.PhantomJS("E:/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe")
    driver.get("")
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





class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(592, 437)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 54, 12))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 71, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 140, 71, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(120, 10, 221, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 50, 221, 31))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 90, 461, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 130, 461, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_1 = QtWidgets.QPushButton(Dialog)
        self.pushButton_1.setGeometry(QtCore.QRect(120, 270, 75, 31))
        self.pushButton_1.clicked.connect(self.web_login)
        self.pushButton_1.setObjectName("pushButton_1")


        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 270, 75, 31))
        self.pushButton_2.clicked.connect(self.go_button)

        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 270, 75, 31))
        self.pushButton_3.clicked.connect(self.re_button)

        self.pushButton_3.setObjectName("pushButton_3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 180, 101, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 230, 121, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(120, 170, 271, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(120, 220, 271, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(370, 30, 211, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(100, 330, 461, 71))
        self.textEdit.setObjectName("textEdit")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(20, 340, 54, 61))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(410, 10, 161, 16))
        self.label_8.setObjectName("label_8")




        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)




    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "自动化挑包工具"))
        self.label.setText(_translate("Dialog", "TS用户名："))
        self.label_2.setText(_translate("Dialog", "TS密码："))
        self.label_3.setText(_translate("Dialog", "修改单编号："))
        self.label_4.setText(_translate("Dialog", "升级文件名："))
        self.lineEdit.setText(_translate("Dialog", ""))
        self.lineEdit_2.setText(_translate("Dialog", ""))
        self.lineEdit_3.setText(_translate("Dialog", ""))
        self.lineEdit_4.setText(_translate("Dialog", ""))
        self.pushButton_1.setText(_translate("Dialog", "登录"))
        self.pushButton_2.setText(_translate("Dialog", "挑包"))
        self.pushButton_3.setText(_translate("Dialog", "打印信息"))
        self.label_5.setText(_translate("Dialog", "压缩包输出路径："))
        self.label_6.setText(_translate("Dialog", "升级文件输出路径："))
        self.lineEdit_5.setText(_translate("Dialog", "D:/raroutput/"))
        self.lineEdit_6.setText(_translate("Dialog", "D:/updatainfo/"))
        self.comboBox.setItemText(0, _translate("Dialog", "HSOBM"))
        self.comboBox.setItemText(1, _translate("Dialog", "IFSManaPlat"))
        self.comboBox.setItemText(2, _translate("Dialog", "IMS"))
        self.comboBox.setItemText(3, _translate("Dialog", "test"))
        self.comboBox.setItemText(4, _translate("Dialog", "TS工具测试"))
        self.comboBox.setItemText(5, _translate("Dialog", "UCF浏览器"
""))
        self.comboBox.setItemText(6, _translate("Dialog", "UFT4us-CFFEX"))
        self.comboBox.setItemText(7, _translate("Dialog", "�ڻ�UFT2.0"))
        self.comboBox.setItemText(8, _translate("Dialog", "业务集中运营平台"))
        self.comboBox.setItemText(9, _translate("Dialog", "互联网理财销售平台ISC"))
        self.comboBox.setItemText(10, _translate("Dialog", "互联网金融接入平台IFS"))
        self.comboBox.setItemText(11, _translate("Dialog", "交易模拟测试平台"))
        self.comboBox.setItemText(12, _translate("Dialog", "信用头寸多活"))
        self.comboBox.setItemText(13, _translate("Dialog", "内存风控平台"))
        self.comboBox.setItemText(14, _translate("Dialog", "刷卡"))
        self.comboBox.setItemText(15, _translate("Dialog", "多金融产品销售平台"
""))
        self.comboBox.setItemText(16, _translate("Dialog", "广发版技术支持测试"
""))
        self.comboBox.setItemText(17, _translate("Dialog", "投行发行系统"))
        self.comboBox.setItemText(18, _translate("Dialog", "撮合交易系统V2.0"))
        self.comboBox.setItemText(19, _translate("Dialog", "新版OTC"))
        self.comboBox.setItemText(20, _translate("Dialog", "新版OTC开发阶段递交包"
""))
        self.comboBox.setItemText(21, _translate("Dialog", "期现UFC2.0"))
        self.comboBox.setItemText(22, _translate("Dialog", "期货2006"))
        self.comboBox.setItemText(23, _translate("Dialog", "期货UF20"))
        self.comboBox.setItemText(24, _translate("Dialog", "期货UFT"))
        self.comboBox.setItemText(25, _translate("Dialog", "期货UFT2.0"))
        self.comboBox.setItemText(26, _translate("Dialog", "期货UFW2.0"))
        self.comboBox.setItemText(27, _translate("Dialog", "期货周边组件"))
        self.comboBox.setItemText(28, _translate("Dialog", "期货策略交易"))
        self.comboBox.setItemText(29, _translate("Dialog", "期货统一账户"))
        self.comboBox.setItemText(30, _translate("Dialog", "期货账户2.0"))
        self.comboBox.setItemText(31, _translate("Dialog", "期货资金管理系统"))
        self.comboBox.setItemText(32, _translate("Dialog", "档案管理平台"))
        self.comboBox.setItemText(33, _translate("Dialog", "法人清算系统"))
        self.comboBox.setItemText(34, _translate("Dialog", "消费支付2.0"))
        self.comboBox.setItemText(35, _translate("Dialog", "热自助"
""))
        self.comboBox.setItemText(36, _translate("Dialog", "独立用户系统V3.0"))
        self.comboBox.setItemText(37, _translate("Dialog", "第3方基金代销测试"))
        self.comboBox.setItemText(38, _translate("Dialog", "经纪业务云平台UF3.0"))
        self.comboBox.setItemText(39, _translate("Dialog", "经纪业务运营平台20"))
        self.comboBox.setItemText(40, _translate("Dialog", "统一接入"))
        self.comboBox.setItemText(41, _translate("Dialog", "统一认证"))
        self.comboBox.setItemText(42, _translate("Dialog", "统一认证系统软件V2.0"))
        self.comboBox.setItemText(43, _translate("Dialog", "统一适当性管理平台"
""))
        self.comboBox.setItemText(44, _translate("Dialog", "综合理财IWM2.0"))
        self.comboBox.setItemText(45, _translate("Dialog", "综合理财标准版V21"))
        self.comboBox.setItemText(46, _translate("Dialog", "网上交易5.0"))
        self.comboBox.setItemText(47, _translate("Dialog", "股票期权"))
        self.comboBox.setItemText(48, _translate("Dialog", "股票期权UFK2.0"))
        self.comboBox.setItemText(49, _translate("Dialog", "股票期权多活UFT"))
        self.comboBox.setItemText(50, _translate("Dialog", "融资融券06版"
""))
        self.comboBox.setItemText(51, _translate("Dialog", "融资融券2.0"))
        self.comboBox.setItemText(52, _translate("Dialog", "融资融券多活UFT"))
        self.comboBox.setItemText(53, _translate("Dialog", "证券极速交易UFT"))
        self.comboBox.setItemText(54, _translate("Dialog", "融资融券06版"
""))
        self.comboBox.setItemText(55, _translate("Dialog", "融资融券2.0"))
        self.comboBox.setItemText(56, _translate("Dialog", "融资融券多活UFT"))
        self.comboBox.setItemText(57, _translate("Dialog", "证券06版"
""))
        self.comboBox.setItemText(58, _translate("Dialog", "证券多活UFT"))
        self.comboBox.setItemText(59, _translate("Dialog", "证券极速交易UFT"))
        self.comboBox.setItemText(60, _translate("Dialog", "账户分析"))
        self.comboBox.setItemText(61, _translate("Dialog", "账户管理2.0"))
        self.comboBox.setItemText(62, _translate("Dialog", "资产存管系统"))
        self.comboBox.setItemText(63, _translate("Dialog", "转融通"
""))
        self.comboBox.setItemText(64, _translate("Dialog", "运维监控"))
        self.comboBox.setItemText(65, _translate("Dialog", "量化投研和交易平台软件1.0"))
        self.comboBox.setItemText(66, _translate("Dialog", "金融基础件"
""))
        self.comboBox.setItemText(67, _translate("Dialog", "银企直连"))
        self.comboBox.setItemText(68, _translate("Dialog", "银证平台"))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">本工具开发源码：https://github.com/dar1122/Autoselect<br>如有疑问，请发邮件致2744544336@qq.com<br>禁止一切商业用途</p></body></html>"))
        self.label_7.setText(_translate("Dialog", "备注："))
        self.label_8.setText(_translate("Dialog", "选择压缩包所在目录"))

    def web_login(self):


        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        self.wlthread = web_login_thread(username,password)

        self.wlthread.start()











    def go_button(self):

        x = self.lineEdit_3.text()
        modification_numbers = x.split(',')
        x1 = self.lineEdit_4.text()
        updata_mumbers = x1.split(',')
        url1 = self.lineEdit_5.text()
        to_path = self.lineEdit_6.text()
        now_comboBox_vaule = self.comboBox.currentText()

        self.gbthread = go_button_thread(now_comboBox_vaule,url1,to_path,modification_numbers,updata_mumbers)
        self.gbthread.start()




    def re_button(self):



        x1 = self.lineEdit_4.text()

        updata_mumbers = x1.split(',')

        to_path = self.lineEdit_6.text()

        updata_info(updata_mumbers,to_path)



class mywidget(Ui_Dialog):
    def __init__(self):

       super().__init__()


class web_login_thread(QtCore.QThread):


    def __init__(self,u,p,parent=None):
        super(web_login_thread,self).__init__(parent)

        self.u = u
        self.p = p

    def run(self):
        from PyQt5.QtWidgets import QMessageBox
        try:
            getTS(self.u,self.p)
        except selenium.common.exceptions.NoSuchElementException:
            print('账号密码有误')


class go_button_thread(QtCore.QThread):
    def __init__(self,a,b,c,d,e,parent=None):
        super(go_button_thread,self).__init__(parent)
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e


    def run(self):
        f_username = cFtp.ftp_username
        f_password = cFtp.ftp_password

        ip = cFtp.ftp_ip
        port = cFtp.ftp_port

        config_url = '/{}/test'.format(self.a)




        ifexit = os.path.isdir(self.b)
        ifexit1 = os.path.isdir(self.c)
        if ifexit == False:
            os.mkdir(self.b)
        if ifexit1 == False:
            os.mkdir(self.c)



        for num in self.d:
            requir_list = []
            a = query(num)
            info1 = updateinfo()
            mod_del()

            name_list = sp_tan(info1)
            for member in name_list:
                for updata_member in self.e:
                    if member == updata_member:
                        new_member = member.split()
                        del new_member[1]
                        requir_list.extend(new_member)

            to_updata_list = requir_list

            webget_url = a
            try:
                url2 = download(ip, port, f_username, f_password, config_url, webget_url,self.b)
                rarto(self.b, url2, to_updata_list,self.c)

            except ftplib.error_perm:
                print('请检查路径ftp路径是否正确')




if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    base = QtWidgets.QWidget()
    w = mywidget()
    w.setupUi(base)
    base.show()
    sys.exit(app.exec_())
