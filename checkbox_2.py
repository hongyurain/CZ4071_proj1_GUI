from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd

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
        return ret
# if __name__ == "__main__":
#     import sys
#     facultyList = pd.read_excel("data/Faculty.xlsx")["Faculty"]
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = checkbox_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())