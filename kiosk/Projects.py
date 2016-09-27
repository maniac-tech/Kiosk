# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Projects.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import Projects_kiosk
import Projects_adc
import Projects_thermalEnergy
import Projects_autonaut
import Projects_oilSpill
import Projects_seaPerch
import Projects_buoy
import Projects_magneticSledge
import Projects_sandBox
import Projects_oyster
import Projects_smartGlass
import Projects_panamaCanal

from Projects_kiosk import Ui_MainWindow1
from Projects_adc import Ui_MainWindow2
from Projects_thermalEnergy import Ui_MainWindow3
from Projects_autonaut import Ui_MainWindow4
from Projects_oilSpill import Ui_MainWindow5
from Projects_seaPerch import Ui_MainWindow6
from Projects_buoy import Ui_MainWindow7
from Projects_magneticSledge import Ui_MainWindow8
from Projects_sandBox import Ui_MainWindow9
from Projects_oyster import Ui_MainWindow10
from Projects_smartGlass import Ui_MainWindow11
from Projects_panamaCanal import Ui_MainWindow12

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

class Ui_MainWindow6(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName(_fromUtf8("MainWindow"))
		MainWindow.resize(845, 575)
		self.centralwidget = QtGui.QWidget(MainWindow)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
		self.gridLayout = QtGui.QGridLayout(self.centralwidget)
		self.gridLayout.setMargin(10)
		self.gridLayout.setSpacing(5)
		self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
		self.scrollArea = QtGui.QScrollArea(self.centralwidget)
		self.scrollArea.setWidgetResizable(True)
		self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
		self.scrollAreaWidgetContents = QtGui.QWidget()
		self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 822, 1142))
		self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
		self.gridLayout_2 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
		self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
		self.label_15 = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.label_15.setText(_fromUtf8(""))
		self.label_15.setPixmap(QtGui.QPixmap(_fromUtf8("E:/Maniac/maniac 2016 documents/Downloads/images.png")))
		self.label_15.setObjectName(_fromUtf8("label_15"))
		self.gridLayout_2.addWidget(self.label_15, 8, 2, 1, 1)
		self.pushButton_12 = QtGui.QPushButton(self.scrollAreaWidgetContents)
		self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
		self.gridLayout_2.addWidget(self.pushButton_12, 7, 2, 1, 1)
		self.pushButton_8 = QtGui.QPushButton(self.scrollAreaWidgetContents)
		self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
		self.gridLayout_2.addWidget(self.pushButton_8, 5, 1, 1, 1)
		self.pushButton_9 = QtGui.QPushButton(self.scrollAreaWidgetContents)
		self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
		self.gridLayout_2.addWidget(self.pushButton_9, 5, 2, 1, 1)
		self.pushButton_10 = QtGui.QPushButton(self.scrollAreaWidgetContents)
		self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
		self.gridLayout_2.addWidget(self.pushButton_10, 7, 0, 1, 1)
		self.pushButton_7 = QtGui.QPushButton(self.scrollAreaWidgetContents)
		self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
		self.gridLayout_2.addWidget(self.pushButton_7, 5, 0, 1, 1)
		self.pushButton_11 = QtGui.QPushButton(self.scrollAreaWidgetContents)
		self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
		self.gridLayout_2.addWidget(self.pushButton_11, 7, 1, 1, 1)
		self.label_13 = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.label_13.setText(_fromUtf8(""))
		self.label_13.setPixmap(QtGui.QPixmap(_fromUtf8("E:/Maniac/maniac 2016 documents/Downloads/images.png")))
		self.label_13.setObjectName(_fromUtf8("label_13"))
		self.gridLayout_2.addWidget(self.label_13, 8, 0, 1, 1)
		self.label_14 = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.label_14.setText(_fromUtf8(""))
		self.label_14.setPixmap(QtGui.QPixmap(_fromUtf8("E:/Maniac/maniac 2016 documents/Downloads/images.png")))
		self.label_14.setObjectName(_fromUtf8("label_14"))
		self.gridLayout_2.addWidget(self.label_14, 8, 1, 1, 1)
		self.pushButton_2 = QtGui.QPushButton(self.scrollAreaWidgetContents)
		self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
		self.gridLayout_2.addWidget(self.pushButton_2, 1, 1, 1, 1)
		self.label = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.label.setText(_fromUtf8(""))
		self.label.setPixmap(QtGui.QPixmap(_fromUtf8("E:/Maniac/maniac 2016 documents/Downloads/images.png")))
		self.label.setObjectName(_fromUtf8("label"))
		self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
		self.label_2 = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.label_2.setText(_fromUtf8(""))
		self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("kiosk.jpg")))
		self.label_2.setObjectName(_fromUtf8("label_2"))
		self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
		self.pushButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		self.gridLayout_2.addWidget(self.pushButton, 1, 0, 1, 1)
		self.label_5 = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.label_5.setText(_fromUtf8(""))
		self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8("E:/Maniac/maniac 2016 documents/Downloads/images.png")))
		self.label_5.setObjectName(_fromUtf8("label_5"))
		self.gridLayout_2.addWidget(self.label_5, 2, 1, 1, 1)
		self.label_4 = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.label_4.setText(_fromUtf8(""))
		self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8("autonaut.jpg")))
		self.label_4.setObjectName(_fromUtf8("label_4"))
		self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
		self.label_9 = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.label_9.setText(_fromUtf8(""))
		self.label_9.setPixmap(QtGui.QPixmap(_fromUtf8("topography.jpg")))
		self.label_9.setObjectName(_fromUtf8("label_9"))
		self.gridLayout_2.addWidget(self.label_9, 4, 2, 1, 1)
		self.label_10 = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.label_10.setText(_fromUtf8(""))
		self.label_10.setPixmap(QtGui.QPixmap(_fromUtf8("ar glasses.jpg")))
		self.label_10.setObjectName(_fromUtf8("label_10"))
		self.gridLayout_2.addWidget(self.label_10, 6, 0, 1, 1)
		self.pushButton_5 = QtGui.QPushButton(self.scrollAreaWidgetContents)
		self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
		self.gridLayout_2.addWidget(self.pushButton_5, 3, 1, 1, 1)
		self.pushButton_3 = QtGui.QPushButton(self.scrollAreaWidgetContents)
		self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
		self.gridLayout_2.addWidget(self.pushButton_3, 1, 2, 1, 1)
		self.pushButton_4 = QtGui.QPushButton(self.scrollAreaWidgetContents)
		self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
		self.gridLayout_2.addWidget(self.pushButton_4, 3, 0, 1, 1)
		self.label_6 = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.label_6.setText(_fromUtf8(""))
		self.label_6.setPixmap(QtGui.QPixmap(_fromUtf8("sea_perch.jpg")))
		self.label_6.setObjectName(_fromUtf8("label_6"))
		self.gridLayout_2.addWidget(self.label_6, 2, 2, 1, 1)
		self.label_8 = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.label_8.setText(_fromUtf8(""))
		self.label_8.setPixmap(QtGui.QPixmap(_fromUtf8("magnetic sledge.jpg")))
		self.label_8.setObjectName(_fromUtf8("label_8"))
		self.gridLayout_2.addWidget(self.label_8, 4, 1, 1, 1)
		self.label_7 = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.label_7.setText(_fromUtf8(""))
		self.label_7.setPixmap(QtGui.QPixmap(_fromUtf8("buoy.JPG")))
		self.label_7.setObjectName(_fromUtf8("label_7"))
		self.gridLayout_2.addWidget(self.label_7, 4, 0, 1, 1)
		self.label_3 = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.label_3.setText(_fromUtf8(""))
		self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("ocean-thermal-energy-conversion-otec-lg.jpg")))
		self.label_3.setObjectName(_fromUtf8("label_3"))
		self.gridLayout_2.addWidget(self.label_3, 0, 2, 1, 1)
		self.label_11 = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.label_11.setText(_fromUtf8(""))
		self.label_11.setPixmap(QtGui.QPixmap(_fromUtf8("oyster.jpg")))
		self.label_11.setObjectName(_fromUtf8("label_11"))
		self.gridLayout_2.addWidget(self.label_11, 6, 1, 1, 1)
		self.pushButton_6 = QtGui.QPushButton(self.scrollAreaWidgetContents)
		self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
		self.gridLayout_2.addWidget(self.pushButton_6, 3, 2, 1, 1)
		self.label_12 = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.label_12.setText(_fromUtf8(""))
		self.label_12.setPixmap(QtGui.QPixmap(_fromUtf8("panama canal 25.jpg")))
		self.label_12.setObjectName(_fromUtf8("label_12"))
		self.gridLayout_2.addWidget(self.label_12, 6, 2, 1, 1)
		self.pushButton_13 = QtGui.QPushButton(self.scrollAreaWidgetContents)
		self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
		self.gridLayout_2.addWidget(self.pushButton_13, 9, 0, 1, 1)
		self.pushButton_14 = QtGui.QPushButton(self.scrollAreaWidgetContents)
		self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
		self.gridLayout_2.addWidget(self.pushButton_14, 9, 1, 1, 1)
		self.pushButton_15 = QtGui.QPushButton(self.scrollAreaWidgetContents)
		self.pushButton_15.setObjectName(_fromUtf8("pushButton_15"))
		self.gridLayout_2.addWidget(self.pushButton_15, 9, 2, 1, 1)
		self.scrollArea.setWidget(self.scrollAreaWidgetContents)
		self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtGui.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 845, 21))
		self.menubar.setObjectName(_fromUtf8("menubar"))
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtGui.QStatusBar(MainWindow)
		self.statusbar.setObjectName(_fromUtf8("statusbar"))
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

		self.window1=None
		self.window2=None
		self.window3=None
		self.window4=None
		self.window5=None
		self.window6=None
		self.window7=None
		self.window8=None
		self.window9=None
		self.window10=None
		self.window11=None
		self.window12=None
		self.window13=None
		self.window14=None
		self.window15=None

		self.pushButton.clicked.connect (self.load_project_kiosk)
		self.pushButton_2.clicked.connect(self.load_project_adc)
		self.pushButton_3.clicked.connect(self.load_project_thermalEnergy)
		self.pushButton_4.clicked.connect(self.load_project_autonaut)
		self.pushButton_5.clicked.connect(self.load_project_oilSpill)
		self.pushButton_6.clicked.connect(self.load_project_seaPerch)
		self.pushButton_7.clicked.connect(self.load_project_buoy)
		self.pushButton_8.clicked.connect(self.load_project_magneticSledge)
		self.pushButton_9.clicked.connect(self.load_project_sandbox)
		self.pushButton_10.clicked.connect(self.load_project_oyster)
		self.pushButton_11.clicked.connect(self.load_project_smartglass)
		self.pushButton_12.clicked.connect(self.load_project_panamaCanal)



	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
		self.pushButton_12.setText(_translate("MainWindow", "Panama Canal", None))
		self.pushButton_8.setText(_translate("MainWindow", "Magnetic Sledge", None))
		self.pushButton_9.setText(_translate("MainWindow", "Sandbox ", None))
		self.pushButton_10.setText(_translate("MainWindow", "Smart Glass", None))
		self.pushButton_7.setText(_translate("MainWindow", "Buoys", None))
		self.pushButton_11.setText(_translate("MainWindow", "Oyester", None))
		self.pushButton_2.setText(_translate("MainWindow", "ADC", None))
		self.pushButton.setText(_translate("MainWindow", "Kiosk", None))
		self.pushButton_5.setText(_translate("MainWindow", "Oil Spill", None))
		self.pushButton_3.setText(_translate("MainWindow", "Thermal Energy", None))
		self.pushButton_4.setText(_translate("MainWindow", "Autonaut", None))
		self.pushButton_6.setText(_translate("MainWindow", "Sea Perch", None))
		self.pushButton_13.setText(_translate("MainWindow", "PushButton", None))
		self.pushButton_14.setText(_translate("MainWindow", "PushButton", None))
		self.pushButton_15.setText(_translate("MainWindow", "PushButton", None))
	
	def load_project_kiosk(self):
		if self.window1==None:
			self.window1 = kioskMainFile()
		self.window1.show()

	def load_project_adc(self):
		if self.window2==None:
			self.window2 = adcMainFile()
		self.window2.show()

	def load_project_thermalEnergy(self):
		if self.window3==None:
			self.window3 = thermalEnergyMainFile()
		self.window3.show()

	def load_project_autonaut(self):
		if self.window4==None:
			self.window4 = autonautMainFile()
		self.window4.show()
		
	def load_project_oilSpill(self):
		if self.window5==None:
			self.window5 = oilSpillMainFile()
		self.window5.show()
	
	def load_project_seaPerch(self):
		if self.window6==None:
			self.window6 = seaPerchMainFile()
		self.window6.show()

	def load_project_buoy(self):
		if self.window7==None:
			self.window7 = buoyMainFile()
		self.window7.show()

	def load_project_magneticSledge(self):
		if self.window8==None:
			self.window8 = magneticSledgeMainFile()
		self.window8.show()

	def load_project_sandbox(self):
		if self.window10==None:
			self.window10 = sandBoxMainFile()
		self.window10.show()

	def load_project_smartglass(self):
		if self.window11==None:
			self.window11 = smartGlassMainFile()
		self.window11.show()

	def load_project_oyster(self):
		if self.window12==None:
			self.window12 = oysterMainFile()
		self.window12.show()

	def load_project_panamaCanal(self):
		if self.window13==None:
			self.window13 = panamaCanalMainFile()
		self.window13.show()

class kioskMainFile (QtGui.QMainWindow, Projects_kiosk.Ui_MainWindow1):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.setupUi(self)

class adcMainFile(QtGui.QMainWindow, Projects_adc.Ui_MainWindow2):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.setupUi(self)

class thermalEnergyMainFile(QtGui.QMainWindow, Projects_thermalEnergy.Ui_MainWindow3):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.setupUi(self)

class autonautMainFile (QtGui.QMainWindow, Projects_autonaut.Ui_MainWindow4):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.setupUi(self)

class oilSpillMainFile (QtGui.QMainWindow, Projects_oilSpill.Ui_MainWindow5):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.setupUi(self)

class seaPerchMainFile (QtGui.QMainWindow, Projects_seaPerch.Ui_MainWindow6):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.setupUi(self)

class buoyMainFile (QtGui.QMainWindow, Projects_buoy.Ui_MainWindow7):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.setupUi(self)

class magneticSledgeMainFile (QtGui.QMainWindow, Projects_magneticSledge.Ui_MainWindow8):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.setupUi(self)

class sandBoxMainFile (QtGui.QMainWindow, Projects_sandBox.Ui_MainWindow9):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.setupUi(self)

class oysterMainFile (QtGui.QMainWindow, Projects_oyster.Ui_MainWindow10):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.setupUi(self)

class smartGlassMainFile (QtGui.QMainWindow, Projects_smartGlass.Ui_MainWindow11):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.setupUi(self)

class panamaCanalMainFile (QtGui.QMainWindow, Projects_panamaCanal.Ui_MainWindow12):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.setupUi(self)



if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	MainWindow = QtGui.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())