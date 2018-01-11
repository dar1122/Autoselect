# coding = utf-8

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit
from PyQt5.QtGui import QIcon
from random import randint
import listtest

class Example(QWidget):

    def __init__(self):

        super().__init__()
        self.initUI()
        self.num = randint(1, 100)

    def initUI(self):

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

    def showMessage(self):

        x = self.text.text()
        listtest.gogogo(x)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())