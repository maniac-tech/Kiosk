import sys
import one
import two
import admin
import about1
import ourtheme
import projects
from PyQt4 import QtGui
from httpWidget import Ui_HttpWidget
from PyQt4 import QtCore, QtGui

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from one import Ui_MainWindow
from two import Ui_MainWindow2
from admin import Ui_MainWindow3
from about1 import Ui_MainWindow4
from ourtheme import Ui_MainWindow5
from projects import Ui_MainWindow6


class Welcome(QtGui.QMainWindow, one.Ui_MainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.setupUi(self)
		self.pushButton.clicked.connect(self.handle1)
		self.window2 = None
		#Button is clicked
		
	def handle1(self):
		if self.window2 is None:
			self.window2 = Mainmenu(self)
		self.window2.show()

class Mainmenu(QtGui.QMainWindow, two.Ui_MainWindow2):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.setupUi(self)
		self.login.clicked.connect(self.adminnew)
		self.about.clicked.connect(self.aboutfn)
		self.theme.clicked.connect(self.themefn)
		self.project.clicked.connect(self.projectfn)
		self.logistics.clicked.connect(self.webfn)
		self.window2 = None
		self.window3 = None
		self.window4 = None
		self.window5 = None
		self.window6 = None
		#Button is clicked

	def adminnew(self):
		if self.window2 is None:
			self.window2= Admin(self)
		self.window2.show()

	def aboutfn(self):
		if self.window3 is None:
			self.window3= About(self)
		self.window3.show()

	def themefn(self):
		if self.window4 is None:
			self.window4=Theme(self)
		self.window4.show()

	def projectfn(self):
		if self.window5 is None:
			self.window5=Projects(self)
		self.window5.show()

	def webfn(self):
		if self.window6 is None:
			self.window6=httpWidget(self)
		self.window6.show()

class Admin(QtGui.QMainWindow, admin.Ui_MainWindow3):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.setupUi(self)

class About(QtGui.QMainWindow, about1.Ui_MainWindow4):
	def __init__(self, parent= None):
		QtGui.QWidget.__init__(self,parent)
		self.setupUi(self)

class Theme(QtGui.QMainWindow, ourtheme.Ui_MainWindow5):
	def __init__(self, parent= None):
		QtGui.QWidget.__init__(self,parent)
		self.setupUi(self)
		self.pushButton_2.clicked.connect(self.homefn)

	def homefn(self):
		self.close()

class Projects(QtGui.QMainWindow, projects.Ui_MainWindow6):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.setupUi(self)
		self.pushButton.clicked.connect(self.handleButton)
		self.window2 = None

	def handleButton(self):
		self.close()
class httpWidget(QtGui.QWidget):
	def __init__(self, parent=None):
		super(httpWidget, self).__init__(parent)
		self.ui = Ui_HttpWidget()
		self.ui.setupUi(self)
		
		# set margins
		l = self.layout()
		l.setMargin(0)
		self.ui.horizontalLayout.setMargin(5)
		
		# set the default
		#url = ''
		#self.ui.url.setText(url)
		
		# load page
		self.ui.webView.load(QtCore.QUrl("http://127.0.0.1/"))
		
		# history buttons:
		self.ui.back.setEnabled(False)
		self.ui.next.setEnabled(False)

		#QtCore.QObject.connect(self.ui.return1,QtCore.SIGNAL("clicked()"), self.return1)
		QtCore.QObject.connect(self.ui.back,QtCore.SIGNAL("clicked()"), self.back)
		QtCore.QObject.connect(self.ui.next,QtCore.SIGNAL("clicked()"), self.next)
		QtCore.QObject.connect(self.ui.url,QtCore.SIGNAL("returnPressed()"), self.url_changed)
		QtCore.QObject.connect(self.ui.webView,QtCore.SIGNAL("linkClicked (const QUrl&)"), self.link_clicked)
		QtCore.QObject.connect(self.ui.webView,QtCore.SIGNAL("urlChanged (const QUrl&)"), self.link_clicked)
		QtCore.QObject.connect(self.ui.webView,QtCore.SIGNAL("loadProgress (int)"), self.load_progress)
		QtCore.QObject.connect(self.ui.webView,QtCore.SIGNAL("titleChanged (const QString&)"), self.title_changed)
		QtCore.QObject.connect(self.ui.reload,QtCore.SIGNAL("clicked()"), self.reload_page)
		QtCore.QObject.connect(self.ui.stop,QtCore.SIGNAL("clicked()"), self.stop_page)
		
		QtCore.QMetaObject.connectSlotsByName(self)
	
	def url_changed(self):
		"""
		Url have been changed by user
		"""
		page = self.ui.webView.page()
		history = page.history()
		if history.canGoBack():
			self.ui.back.setEnabled(True)
		else:
			self.ui.back.setEnabled(False)
		if history.canGoForward():
			self.ui.next.setEnabled(True)
		else:
			self.ui.next.setEnabled(False)
		
		url = self.ui.url.text()
		self.ui.webView.setUrl(QtCore.QUrl(url))
		
	def stop_page(self):
		"""
		Stop loading the page
		"""
		self.ui.webView.stop()
	
	def title_changed(self, title):
		"""
		Web page title changed - change the tab name
		"""
		self.setWindowTitle(title)
	
	def reload_page(self):
		"""
		Reload the web page
		"""
		self.ui.webView.setUrl(QtCore.QUrl(self.ui.url.text()))
	
	def link_clicked(self, url):
		"""
		Update the URL if a link on a web page is clicked
		"""
		page = self.ui.webView.page()
		history = page.history()
		if history.canGoBack():
			self.ui.back.setEnabled(True)
		else:
			self.ui.back.setEnabled(False)
		if history.canGoForward():
			self.ui.next.setEnabled(True)
		else:
			self.ui.next.setEnabled(False)
		
		self.ui.url.setText(url.toString())
	
	def load_progress(self, load):
		"""
		Page load progress
		"""
		if load == 100:
			self.ui.stop.setEnabled(False)
		else:
			self.ui.stop.setEnabled(True)
		
	def back(self):
		self.close()
	
	def next(self):
		"""
		Next button clicked, go to next page
		"""
		page = self.ui.webView.page()
		history = page.history()
		history.forward()
		if history.canGoForward():
			
			self.ui.next.setEnabled(True)
		else:
			self.ui.next.setEnabled(False)

	#def return1(self):
		#self.close()

		
if  __name__ == '__main__':

	import sys
	app = QtGui.QApplication(sys.argv)
	window = Welcome()
	window.show()
	sys.exit(app.exec_())