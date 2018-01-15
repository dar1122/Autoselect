# coding = utf-8

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
from random import randint
from PyQt5 import QtWidgets


class Example(QWidget):

    def __init__(self):

        super().__init__()
        self.initUI()
        self.num = randint(1, 100)

    def initUI(self):


        self.label_2 = QtWidgets.QLabel()
        self.label_2.setGeometry(QtCore.QRect(10, 60, 54, 12))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel()
        self.label_3.setGeometry(QtCore.QRect(10, 100, 71, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel()
        self.label_4.setGeometry(QtCore.QRect(10, 140, 71, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit()
        self.lineEdit.setGeometry(QtCore.QRect(120, 10, 221, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit()
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 50, 221, 31))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit()
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 90, 461, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit()
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 130, 461, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_1 = QtWidgets.QPushButton()
        self.pushButton_1.setGeometry(QtCore.QRect(120, 270, 75, 31))

        self.pushButton_1.setObjectName("pushButton_1")

        self.pushButton_2 = QtWidgets.QPushButton()
        self.pushButton_2.setGeometry(QtCore.QRect(210, 270, 75, 31))


        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton()
        self.pushButton_3.setGeometry(QtCore.QRect(300, 270, 75, 31))


        self.pushButton_3.setObjectName("pushButton_3")
        self.label_5 = QtWidgets.QLabel()
        self.label_5.setGeometry(QtCore.QRect(10, 180, 101, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel()
        self.label_6.setGeometry(QtCore.QRect(10, 230, 121, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit_5 = QtWidgets.QLineEdit()
        self.lineEdit_5.setGeometry(QtCore.QRect(120, 170, 271, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit()
        self.lineEdit_6.setGeometry(QtCore.QRect(120, 220, 271, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.comboBox = QtWidgets.QComboBox()
        self.comboBox.setGeometry(QtCore.QRect(370, 30, 211, 31))
        self.comboBox.setObjectName("comboBox")

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('学点编程吧--猜数字')
        self.setWindowIcon(QIcon('xdbcb8.ico'))

        self.bt1 = QPushButton('我猜', self)
        self.bt1.setGeometry(115, 150, 70, 30)
        self.bt1.setToolTip('<b>点击这里猜数字</b>')
        self.bt1.clicked.connect(self.showMessage)

        self.text = QLineEdit('在这里输入数字', self)
        self.text.selectAll()
        self.text.setFocus()
        self.text.setGeometry(80, 50, 150, 30)
















        self.show()

    def er(self):
        from PyQt5.QtWidgets import QMessageBox
        QMessageBox.about(self,'ddd','error')

    def showMessage(self):
        try:
            a = 5
            b = 's'
            if a>b:
                print('ok')
        except TypeError:
            self.er()






if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())