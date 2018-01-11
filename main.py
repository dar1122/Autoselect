from PyQt5 import QtWidgets
from dar import Ui_Dialog

class mywidget(Ui_Dialog):
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