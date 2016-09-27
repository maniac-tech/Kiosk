# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'two.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1366, 766)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet(_fromUtf8("background-image: url(bg2.jpg);"))
        MainWindow.setAnimated(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 120, 5, 13))
        self.label.setStyleSheet(_fromUtf8("background: transparent;"))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("E:/Maniac/maniac 2016 documents/Downloads/logo.png")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(440, 120, 481, 421))
        self.textBrowser.setStyleSheet(_fromUtf8("background: transparent;\n"
"background-image:url(logo1.png);"))
        self.textBrowser.setFrameShape(QtGui.QFrame.NoFrame)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.theme = QtGui.QPushButton(self.centralwidget)
        self.theme.setGeometry(QtCore.QRect(100, 310, 220, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Myriad Pro"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.theme.setFont(font)
        self.theme.setStyleSheet(_fromUtf8(" background:transparent;\n"
" background-color: rgb(90, 197, 197);\n"
" color:rgb(74, 94, 93);\n"
"\n"
"font: 75 18pt \"Myriad Pro\";\n"
"\n"
" border-width:60px;\n"
" border-radius:15px;\n"
" max-width:220px;\n"
" max-height:50px;\n"
" min-width:220px;\n"
" min-height:50px;"))
        self.theme.setObjectName(_fromUtf8("theme"))
        self.logistics = QtGui.QPushButton(self.centralwidget)
        self.logistics.setGeometry(QtCore.QRect(1060, 180, 220, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Myriad Pro"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.logistics.setFont(font)
        self.logistics.setStyleSheet(_fromUtf8(" background:transparent;\n"
" background-color: rgb(90, 197, 197);\n"
" color:rgb(74, 94, 93);\n"
"\n"
"font: 75 18pt \"Myriad Pro\";\n"
"\n"
" border-width:60px;\n"
" border-radius:15px;\n"
" max-width:220px;\n"
" max-height:50px;\n"
" min-width:220px;\n"
" min-height:50px;\n"
"\n"
""))
        self.logistics.setObjectName(_fromUtf8("logistics"))
        self.about = QtGui.QPushButton(self.centralwidget)
        self.about.setGeometry(QtCore.QRect(1060, 440, 220, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Myriad Pro"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.about.setFont(font)
        self.about.setStyleSheet(_fromUtf8(" background:transparent;\n"
" background-color: rgb(90, 197, 197);\n"
" color:rgb(74, 94, 93);\n"
"\n"
"font: 75 18pt \"Myriad Pro\";\n"
"\n"
" border-width:60px;\n"
" border-radius:15px;\n"
" max-width:220px;\n"
" max-height:50px;\n"
" min-width:220px;\n"
" min-height:50px;"))
        self.about.setObjectName(_fromUtf8("about"))
        self.login = QtGui.QPushButton(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(1060, 310, 220, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Myriad Pro"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.login.setFont(font)
        self.login.setStyleSheet(_fromUtf8(" background:transparent;\n"
" background-color: rgb(90, 197, 197);\n"
" color:rgb(74, 94, 93);\n"
"\n"
"font: 75 18pt \"Myriad Pro\";\n"
"\n"
" border-width:60px;\n"
" border-radius:15px;\n"
" max-width:220px;\n"
" max-height:50px;\n"
" min-width:220px;\n"
" min-height:50px;\n"
""))
        self.login.setObjectName(_fromUtf8("login"))
        self.events = QtGui.QPushButton(self.centralwidget)
        self.events.setGeometry(QtCore.QRect(100, 440, 220, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Myriad Pro"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.events.setFont(font)
        self.events.setStyleSheet(_fromUtf8(" background:transparent;\n"
" background-color: rgb(90, 197, 197);\n"
" color:rgb(74, 94, 93);\n"
"\n"
"font: 75 18pt \"Myriad Pro\";\n"
"\n"
" border-width:60px;\n"
" border-radius:15px;\n"
" max-width:220px;\n"
" max-height:50px;\n"
" min-width:220px;\n"
" min-height:50px;"))
        self.events.setObjectName(_fromUtf8("events"))
        self.project = QtGui.QPushButton(self.centralwidget)
        self.project.setGeometry(QtCore.QRect(100, 180, 220, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Myriad Pro"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.project.setFont(font)
        self.project.setStyleSheet(_fromUtf8(" background:transparent;\n"
" background-color: rgb(90, 197, 197);\n"
" color:rgb(74, 94, 93);\n"
"\n"
"font: 75 18pt \"Myriad Pro\";\n"
"\n"
" border-width:60px;\n"
" border-radius:15px;\n"
" max-width:220px;\n"
" max-height:50px;\n"
" min-width:220px;\n"
" min-height:50px;\n"
""))
        self.project.setObjectName(_fromUtf8("project"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.theme.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">wqeqrqwr</span></p></body></html>", None))
        self.theme.setText(_translate("MainWindow", "THEME", None))
        self.logistics.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">cLICK KAR NAHI TOH GAAND MAARUNGA!!</span></p></body></html>", None))
        self.logistics.setText(_translate("MainWindow", "LOGISTICS", None))
        self.about.setToolTip(_translate("MainWindow", "<html><head/><body><p>cLICK KAR NAHI TOH GAAND MAARUNGA!!</p></body></html>", None))
        self.about.setText(_translate("MainWindow", "ABOUT", None))
        self.login.setToolTip(_translate("MainWindow", "<html><head/><body><p>cLICK KAR NAHI TOH GAAND MAARUNGA!!</p></body></html>", None))
        self.login.setText(_translate("MainWindow", "LOGIN", None))
        self.events.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">wqeqrqwr</span></p></body></html>", None))
        self.events.setText(_translate("MainWindow", "EVENTS", None))
        self.project.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">wqeqrqwr</span></p></body></html>", None))
        self.project.setText(_translate("MainWindow", "PROJECTS", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

