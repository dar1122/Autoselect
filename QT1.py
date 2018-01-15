# coding = utf-8
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton, QLineEdit, QHBoxLayout,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication,QRect
import listtest


class Ico(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        _translate = QCoreApplication.translate


        self.comboBox.setGeometry(QRect(370, 30, 211, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, _translate("Dialog", "HSOBM"))
        self.comboBox.setItemText(1, _translate("Dialog", "IFSManaPlat"))
        self.comboBox.setItemText(2, _translate("Dialog", "IMS"))

        self.setGeometry(600,600,600,440)
        self.setWindowTitle('自动化挑包工具')
        self.setWindowIcon(QIcon('1.jpg'))



        qbtn = QPushButton('退出',self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)

        start_button = QPushButton('开始',self)
        start_button.clicked.connect()

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








        self.show()











if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ico()


    sys.exit(app.exec_())