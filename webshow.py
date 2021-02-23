import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
app = QApplication(sys.argv)
web = QWebEngineView()
web.load(QUrl('http://127.0.0.1:8080/'))
web.show()
sys.exit(app.exec_())