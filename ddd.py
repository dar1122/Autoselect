# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ddd.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(160, 120, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.button)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "PushButton"))

    def button(self):

        QMessageBox.about(self,'sss','sss')

class mywidget(Ui_Form):
    def __init__(self,parent=None):

        pass
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    base = QtWidgets.QWidget()
    w = mywidget()
    w.setupUi(base)
    base.show()
    sys.exit(app.exec_())