# coding = utf-8
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QMessageBox,QLineEdit,QDialog,QLabel,QHBoxLayout,QVBoxLayout,QInputDialog
from PyQt5.QtGui import QIcon,QKeyEvent,QKeySequence,QRegExpValidator
from PyQt5.QtCore import QCoreApplication,Qt,QEvent,QRegExp
import listtest

class Ico(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(600,600,600,440)
        self.setWindowTitle('自动化挑包工具')
        self.setWindowIcon(QIcon('1.jpg'))

        qbtn = QPushButton('退出',self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)

        start_button = QPushButton('开始',self)
        start_button.clicked.connect(listtest.gogogo)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(start_button)
        hbox.addWidget(qbtn)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.text = QLineEdit('dar',self)


        self.text.setGeometry(30,60,150,50)






        self.text1 = QLineEdit(self)
        self.text1.setGeometry(250,60,150,50)






        self.show()









if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ico()


    sys.exit(app.exec_())