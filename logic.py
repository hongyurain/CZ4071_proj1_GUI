import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
# from PyQt5.QtWebEngineWidgets import *
import pandas as pd

from windows import Ui_MainWindow, Ui_Dialog
from checkbox_2 import checkbox_Dialog

class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
    def myWindow(self):
        self.hide()
        self.myWin = MyWindow()
        self.myWin.show()

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        gridLayout = QGridLayout(centralWidget)
        gridLayout.addWidget(self.ui.label,      1, 0, alignment=Qt.AlignCenter)
        gridLayout.addWidget(self.ui.label_2,    0, 0, alignment=Qt.AlignCenter)
        gridLayout.addWidget(self.ui.pushButton, 6, 0)
        gridLayout.addWidget(self.ui.pushButton2, 5, 0)
        gridLayout.addWidget(self.ui.comboBox, 2, 0)
        gridLayout.addWidget(self.ui.comboBox2, 3, 0)
        gridLayout.addWidget(self.ui.comboBox3, 4, 0)

    def dialogbox(self):
        self.hide()
        self.myDialog = MyDialog()
        self.myDialog.show()
    def checkbox(self):
        self.hide()
        self.cb = checkbox_Dialog()
        self.cb.setupUi(QDialog())
        self.cb.show()

    def updateGraph(self, i):
        if i==0:
            pass
        elif i==1:
            self.hide()
            self.myDialog = MyDialog()
            self.myDialog.show()
        elif i==2:
            #app = QApplication(sys.argv)
            #self.hide()
            QDesktopServices.openUrl(QUrl('http://127.0.0.1:8080/'))

            # web = QWebEngineView()
            # web.resize(640,480)
            # web.load(QUrl('https://www.google.com/'))
            # web.show()
            #sys.exit(app.exec_())
        elif i==3:
            pass
        elif i==4:
            pass
        elif i==5:
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    facultyList = pd.read_excel("data/Faculty.xlsx")["Faculty"]
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())