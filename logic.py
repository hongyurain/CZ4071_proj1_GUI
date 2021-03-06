import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
# from PyQt5.QtWebEngineWidgets import *
import pandas as pd
from preprocessing import generate_graph

from windows import Ui_MainWindow, Ui_Dialog, checkbox_Dialog, \
    newFacultyDialog, propertyDialog, analyzeDialog, facultyMemDialog
#from checkbox_2 import checkbox_Dialog

class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
    def myWindow(self):
        self.hide()
        self.myWin = MyWindow()
        self.myWin.show()
class newFalDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = newFacultyDialog()
        self.ui.setupUi(self)
    def myWindow(self):
        self.hide()
        self.myWin = MyWindow()
        self.myWin.show()
class FalMemDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = facultyMemDialog()
        self.ui.setupUi(self)
    def myWindow(self):
        self.hide()
        self.myWin = MyWindow()
        self.myWin.show()

class propertyDia(QDialog):
    def __init__(self, i):
        super().__init__()
        self.ui = propertyDialog()
        self.ui.setupUi(self, i)
    def myWindow(self):
        self.hide()
        self.myWin = MyWindow()
        self.myWin.show()
class AnalyzeDia(QDialog):
    def __init__(self, i):
        super().__init__()
        self.ui = analyzeDialog()
        self.ui.setupUi(self, i)
    def myWindow(self):
        self.hide()
        self.myWin = MyWindow()
        self.myWin.show()
class CheckBox(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = checkbox_Dialog()
        self.ui.setupUi(self)
    def myWindow(self):
        self.hide()
        self.myWin = MyWindow()
        self.myWin.show()
    def falcultyMem(self):
        self.hide()
        self.new = FalMemDialog()
        self.new.show()
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

    def newFacultyD(self):
        self.hide()
        self.myDialog2 = newFalDialog()
        self.myDialog2.show()
    def facultyMemD(self):
        self.hide()
        self.myDialog2 = FalMemDialog()
        self.myDialog2.show()

    def propertyD(self, i):
        if i==0:
            pass
        else:
            self.hide()
            self.myDialog3 = propertyDia(i)
            self.myDialog3.show()

    def analyzeD(self, i):
        if i==0:
            pass
        else:
            self.hide()
            self.myDialog4 = AnalyzeDia(i)
            self.myDialog4.show()

    def checkbox(self):
        self.hide()
        self.cb = CheckBox()
        self.cb.show()

    def updateGraph(self, i):
        if i==0:
            pass
        else:
            year=2000+i-1
            print("chose year: ",year)
            QDesktopServices.openUrl(QUrl('http://127.0.0.1:8080/'))
        # elif i==1:
        #     self.hide()
        #     self.myDialog = MyDialog()
        #     self.myDialog.show()
        # elif i==2:
        #     #app = QApplication(sys.argv)
        #     #self.hide()
        #     QDesktopServices.openUrl(QUrl('http://127.0.0.1:8080/'))
        #
        #     # web = QWebEngineView()
        #     # web.resize(640,480)
        #     # web.load(QUrl('https://www.google.com/'))
        #     # web.show()
        #     #sys.exit(app.exec_())
        # elif i==3:
        #     pass
        # elif i==4:
        #     pass
        # elif i==5:
        #     pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    facultyList = pd.read_excel("data/Faculty.xlsx")["Faculty"]
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())