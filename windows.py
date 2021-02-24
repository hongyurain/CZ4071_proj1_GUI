from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pandas as pd

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 260, 800, 150))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByMouse)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 300, 200, 27))
        self.pushButton.setObjectName("pushButton")
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 300, 200, 27))
        self.pushButton.setObjectName("pushButton2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 850, 150))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(50, 290, 611, 51))
        self.comboBox.setObjectName("comboBox")
        for i in range(23):
            self.comboBox.addItem("")
        self.comboBox2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox2.setGeometry(QtCore.QRect(50, 290, 611, 51))
        self.comboBox2.setObjectName("comboBox2")
        for i in range(4):
            self.comboBox2.addItem("")
        self.comboBox3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox3.setGeometry(QtCore.QRect(50, 290, 611, 51))
        self.comboBox3.setObjectName("comboBox3")
        for i in range(5):
            self.comboBox3.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 685, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.checkbox)
        self.pushButton2.clicked.connect(MainWindow.dialogbox)
        self.comboBox.currentIndexChanged.connect(MainWindow.updateGraph)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p align=\"center\"><span style=\" "
                                      "font-weight:600; color:#ff0000;\">"
                                      "Welcome to NTU SCSE network analysis system</span>"
                                      "</p><p align=\"center\">Brought to you by Group : "
                                      "<span style=\" font-style:italic;\">Xia Chenguang, Zhang Xinyi,"
                                      " Zhou Hongyu, Hu Wenqi</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">"
                                                     "<img src=\"pictures/network_3_720x160.jpg\"/>"
                                                     "</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Select faculty members"))
        self.pushButton2.setText(_translate("MainWindow", "Add new faculty"))
        selectYearText = ["Select one", "show network until year 2000"]
        questionList = ["Select one", "p1", "p2", "p3"]
        options = ["Select one", "collaboration between faculty of different ranks",
                   "collaboration between faculty holding or held management position and non-management faculty",
                   "collaboration between faculty of different areas in computer science",
                   "are central nodes of the network measured using network properties identical to excellence nodes"]
        for i in range(2001, 2022):
            selectYearText.append("show network until year "+str(i))
        for i in range(23):
            self.comboBox.setItemText(i, _translate("Interface", selectYearText[i]))
        for i in range(4):
            self.comboBox2.setItemText(i, _translate("Interface", questionList[i]))
        for i in range(5):
            self.comboBox3.setItemText(i, _translate("Interface", options[i]))
        file = pd.read_excel("data/Faculty.xlsx")
        facultyList = file["Faculty"]


class Ui_Dialog(object):
    def setupUi(self, Dialog2):
        Dialog2.setObjectName("Dialog2")
        Dialog2.resize(835, 549)
        self.label_2 = QtWidgets.QLabel(Dialog2)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 751, 401))
        self.label_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("pictures/graph2.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog2)
        self.label_3.setGeometry(QtCore.QRect(31, 35, 311, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog2)
        self.label_4.setGeometry(QtCore.QRect(110, 20, 641, 31))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.widget = QtWidgets.QWidget(Dialog2)
        self.widget.setGeometry(QtCore.QRect(30, 480, 751, 61))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.spinBox = QtWidgets.QSpinBox(self.widget)
        self.spinBox.setMinimum(2000)
        self.spinBox.setMaximum(2021)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.widget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog2)
        self.buttonBox.accepted.connect(Dialog2.myWindow)
        self.buttonBox.rejected.connect(Dialog2.myWindow)
        self.pushButton.clicked.connect(self.label_2.update)
        QtCore.QMetaObject.connectSlotsByName(Dialog2)

    def retranslateUi(self, Dialog2):
        _translate = QtCore.QCoreApplication.translate
        Dialog2.setWindowTitle(_translate("Dialog2", "Dialog"))
        self.label_3.setText(_translate("Dialog2", "Graph"))
        self.label_4.setText(_translate("Dialog2", "Evolvement of network since year 2000"))
        self.label.setText(_translate("Dialog2", "select year"))
        self.pushButton.setText(_translate("Dialog2", "Load graph"))


class checkbox_Dialog(object):

    def setupUi(self, Dialog):
        self.facultyList = pd.read_excel("data/Faculty.xlsx")["Faculty"]
        Dialog.setObjectName("Dialog")
        Dialog.resize(501, 350)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setMinimumSize(QtCore.QSize(200, 50))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 474, 348))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.okButton = QtWidgets.QPushButton(Dialog)
        self.okButton.setGeometry(QtCore.QRect(230, 40, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.okButton.setFont(font)
        self.okButton.setObjectName("okButton")
        self.okButton.clicked.connect(self.findState)
        self.okButton.clicked.connect(Dialog.myWindow)
        for i in range(1,18):
            exec("""self.horizontalLayout_{} = QtWidgets.QHBoxLayout()
self.horizontalLayout_{}.setObjectName("horizontalLayout_{}")
self.checkbox_{} = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
self.checkbox_{}.setObjectName("{}")
self.horizontalLayout_{}.addWidget(self.checkbox_{})
self.checkbox_{} = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
self.checkbox_{}.setObjectName("{}")
self.horizontalLayout_{}.addWidget(self.checkbox_{})
self.checkbox_{} = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
self.checkbox_{}.setObjectName("{}")
self.horizontalLayout_{}.addWidget(self.checkbox_{})
self.checkbox_{} = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
self.checkbox_{}.setObjectName("{}")
self.horizontalLayout_{}.addWidget(self.checkbox_{})
self.checkbox_{} = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
self.checkbox_{}.setObjectName("{}")
self.horizontalLayout_{}.addWidget(self.checkbox_{})
self.gridLayout.addLayout(self.horizontalLayout_{}, {}, 0, 1, 1)
            """.format(i,i,i,(i-1)*5,(i-1)*5,self.facultyList[(i-1)*5],i,(i-1)*5,
                       (i-1)*5+1,(i-1)*5+1,self.facultyList[(i-1)*5+1],i,(i-1)*5+1,
                       (i-1)*5+2,(i-1)*5+2,self.facultyList[(i-1)*5+2],i,(i-1)*5+2,
                       (i-1)*5+3,(i-1)*5+3,self.facultyList[(i-1)*5+3],i,(i-1)*5+3,
                       (i - 1) * 5+4, (i - 1) * 5+4, self.facultyList[(i - 1) * 5+4], i, (i - 1) * 5+4,
                       i, i-1))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.okButton.setText(_translate("Dialog", "ok"))
        for i in range(85):
            exec("""self.checkbox_{}.setText(_translate("Dialog", "{}"))""".format(i,self.facultyList[i]))

    def findState(self):
        ret = []
        for i in range(85):
            exec("""if self.checkbox_{}.isChecked():
    ret.append(self.checkbox_{}.text())""".format(i, i))
        print(ret)
        QDesktopServices.openUrl(QUrl('http://127.0.0.1:8080/'))
        return ret