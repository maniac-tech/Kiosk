import sys
import one
import admin
import newabout
import ourtheme3
import Projects
import events
import RegisterForm
import RegisterTy

from httpWidget import Ui_HttpWidget

from admin import Ui_MainWindow3
from newabout import Ui_MainWindow4
from ourtheme3 import Ui_MainWindow5
from one import Ui_MainWindow
from events import Ui_MainWindow9
from Projects import Ui_MainWindow6
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QTimeLine
from PyQt4.QtGui import *
from RegisterForm import Ui_MainWindow8
from RegisterTy import Ui_MainWindow10
import pymysql.cursors

class FaderWidget(QWidget):

	def __init__(self, old_widget, new_widget):
	
		QWidget.__init__(self, new_widget)
		
		self.old_pixmap = QPixmap(new_widget.size())
		old_widget.render(self.old_pixmap)
		self.pixmap_opacity = 1.0
		
		self.timeline = QTimeLine()
		self.timeline.valueChanged.connect(self.animate)
		self.timeline.finished.connect(self.close)
		self.timeline.setDuration(333)
		self.timeline.start()
		
		self.resize(new_widget.size())
		self.show()
	
	def paintEvent(self, event):
	
		painter = QPainter()
		painter.begin(self)
		painter.setOpacity(self.pixmap_opacity)
		painter.drawPixmap(0, 0, self.old_pixmap)
		painter.end()
	
	def animate(self, value):
	
		self.pixmap_opacity = 1.0 - value
		self.repaint()

class StackedWidget(QStackedWidget):

	def __init__(self, parent = None):
		QStackedWidget.__init__(self, parent)
	
	def setCurrentIndex(self, index):
		self.fader_widget = FaderWidget(self.currentWidget(), self.widget(index))
		QStackedWidget.setCurrentIndex(self, index)
	
	def setPage1(self):
		self.setCurrentIndex(0)
	
	def setPage2(self):
		self.setCurrentIndex(1)

	def setPage3(self):
		self.setCurrentIndex(2)

	def setPage4(self):
		self.setCurrentIndex(3)

	def setPage5(self):
		self.setCurrentIndex(4)

	def setPage6(self):
		self.setCurrentIndex(5)

	


class Projects(QtGui.QMainWindow, Projects.Ui_MainWindow6):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.setupUi(self)

class Theme(QtGui.QMainWindow, ourtheme3.Ui_MainWindow5):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.setupUi(self)


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
		#QtCore.QObject.connect(self.ui.back,QtCore.SIGNAL("clicked()"), self.back)
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


class About(QtGui.QMainWindow, newabout.Ui_MainWindow4):
	def __init__(self, parent= None):
		QtGui.QWidget.__init__(self,parent)
		self.setupUi(self)
	
class Login(QtGui.QMainWindow, RegisterForm.Ui_MainWindow8):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.setupUi(self)
		self.pushButton_2.clicked.connect(self.fingerprint)
		self.pushButton.clicked.connect(self.SQLQuery)
		self.window2 = None


	def new(self):
		print("new")
	
	def main1(self):
		for z in range(0,256):
			if z in lst: 
				z=z+1
				self.new()
			else:
				lst.append(z)
				a=z
				z=z+1
				break
		return a

	def finger_call_main(self):
		a= self.main1()
		print("printing a")
		#print(a)
		#for x in lst:
			#print (x)

	def printx(self,l):
		for i in l:
			print (i)
		print ('')

	def readpacket(self):
		time.sleep(1)
		w = ser.inWaiting()
		ret = []
		if w >= 9:
			s = ser.read(9) #partial read to get length
			ret.extend(struct.unpack('!HIBH', s))
			ln = ret[-1]
			
			time.sleep(1)
			w = ser.inWaiting()
			if w >= ln:
				s = ser.read(ln)
				form = '!' + 'B' * (ln - 2) + 'H'
				ret.extend(struct.unpack(form, s))
		return ret


	def writePacket(self,data):
		pack2 = pack + [(len(data) + 2)]
		a = sum(pack2[-2:] + data)
		pack_str = '!HIBH' + 'B' * len(data) + 'H'
		l = pack2 + data + [a]
		s = struct.pack(pack_str, *l)
		#print("Writepacket S value: " +s)
		ser.write(s)


	def verifyFinger(self):
		data = [0x13, 0x0, 0, 0, 0]
		self.writePacket(data)
		s = self.readpacket()
		return s[4]
			
	def genImg(self):
		data = [0x1]
		self.writePacket(data)
		s = self.readpacket()
		return s[4] 

	def img2Tz(self,buf):
		data = [0x2, buf]
		self.writePacket(data)
		s = self.readpacket()
		return s[4]

	def regModel(self):
		 data = [0x5]
		 self.writePacket(data)
		 s = self.readpacket()
		 return s[4]

	def store(self,id):
		data = [0x6, 0x1, 0x0, id]
		self.writePacket(data)
		s = self.readpacket()
		return s[4]

	

	def search(self):
		data = [0x4, 0x1, 0x0, 0x0, 0x0, 0x5]
		self.writePacket(data)
		s = self.readpacket()
		return s[4:-1]	
	
	
	
	
		
	def fingerprint(self):
		if self.verifyFinger():
			print ('Verification Error1')
			sys.exit(0)

		print ('Put finger')
		sys.stdout.flush()

		time.sleep(1)   
		while self.genImg():
			time.sleep(0.1)

			print ('.')
			sys.stdout.flush()

		print ('')
		sys.stdout.flush()

		if self.img2Tz(1):
			print ('Conversion Error')
			sys.exit(0)

		print ('Put finger again')
		sys.stdout.flush()

		time.sleep(1)   
		while self.genImg():
			time.sleep(0.1)
			print ('.')
			sys.stdout.flush()

		print ('')
		sys.stdout.flush()

		if self.img2Tz(2):
			print ('Conversion Error')
			sys.exit(0)

		if self.regModel():
			print ('Template Error')
			sys.exit(0)

		id=self.main1()

		if self.store(id):
			print ('Store Error')
			sys.exit(0) 
		self.lineEdit.setText("Enrolled successfully at id %d"%id)

		print ("Enrolled successfully at id %d"%id)

	def mainfuncn(self):
		if self.verifyFinger():
			print( 'Verification Error')
			sys.exit(-1)

		print('Put finger')
		sys.stdout.flush()

		time.sleep(1)	
		for _ in range(5):
			g = self.genImg()
			if g == 0:
				break
			#time.sleep(1)

			print( '.')
			sys.stdout.flush()

		print( '')
		sys.stdout.flush()
		if g != 0:
			sys.exit(-1)

		if self.img2Tz(1):
			print('Conversion Error')
			sys.exit(-1)

		r = self.search()
		print('Search result', r)
		if r[0] == 0 and r[2] in lst:
			print('Successful')
			
		else:
			print('Unsuccessful')

	def SQLQuery(self):
		#SQL QUERY PART ONLY.
		# Open database connection
		db = pymysql.connect("localhost","root","","testsept" )

		# prepare a cursor object using cursor() method
		cursor = db.cursor()

		#fetching the input and storing in the variables
		name=self.plainTextEdit.toPlainText()
		emailId=self.plainTextEdit_2.toPlainText()
		branch=self.plainTextEdit_3.toPlainText()
		contact=self.plainTextEdit_4.toPlainText()

		try:
		   # Execute the SQL command
		   cursor.execute("""INSERT INTO registerForm(name,
				 emailId, branch, contact)
				 VALUES (%s, %s , %s , %s)""",(name,emailId,branch,contact))
		   # Commit your changes in the database
		   db.commit()
		except:
		   # Rollback in case there is any error
		   db.rollback()

		# disconnect from server
		db.close()

		#SQL QUERY PART HAS ENDED

		#Loading the Dialog Box
		if self.window2 is None:
			self.window2 = DialogBox(self)
		self.window2.show()

class DialogBox(QtGui.QMainWindow, RegisterTy.Ui_MainWindow10):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.setupUi(self)


class Events(QtGui.QMainWindow,events.Ui_MainWindow9 ):
	def __init__(self, parent= None):
		QtGui.QWidget.__init__(self,parent)
		self.setupUi(self)

	def start(num):
		window = QWidget()
		window.showMaximized()
		stack = StackedWidget()
	
	if num==1:
		logged_in_widget = Projects()
		stack.addWidget(logged_in_widget)
		logistics = httpWidget()
		stack.addWidget(logistics)
		theme= Theme()
		stack.addWidget(theme)
		about = About()
		stack.addWidget(about)
		events=Events()
		stack.addWidget(events)
		login=Login()
		stack.addWidget(login)

	if num==2:
		logistics = httpWidget()
		stack.addWidget(logistics)
		logged_in_widget = Projects()
		stack.addWidget(logged_in_widget)
		theme= Theme()
		stack.addWidget(theme)
		about = About()
		stack.addWidget(about)
		events=Events()
		stack.addWidget(events)
		login=Login()
		stack.addWidget(login)

	if num==3:
		theme= Theme()
		stack.addWidget(theme)
		logistics = httpWidget()
		stack.addWidget(logistics)
		logged_in_widget = Projects()
		stack.addWidget(logged_in_widget)
		about = About()
		stack.addWidget(about)
		events=Events()
		stack.addWidget(events)
		login=Login()
		stack.addWidget(login)

	if num==4:
		about = About()
		stack.addWidget(about)
		logged_in_widget = Projects()
		stack.addWidget(logged_in_widget)
		logistics = httpWidget()
		stack.addWidget(logistics)
		theme= Theme()
		stack.addWidget(theme)
		events=Events()
		stack.addWidget(events)
		login=Login()
		stack.addWidget(login)

	if num==5:
		events=Events()
		stack.addWidget(events)
		logged_in_widget = Projects()
		stack.addWidget(logged_in_widget)
		logistics = httpWidget()
		stack.addWidget(logistics)
		theme= Theme()
		stack.addWidget(theme)
		about = About()
		stack.addWidget(about)
		login=Login()
		stack.addWidget(login)

	if num==6:
		login=Login()
		stack.addWidget(login)
		logged_in_widget = Projects()
		stack.addWidget(logged_in_widget)
		logistics = httpWidget()
		stack.addWidget(logistics)
		theme= Theme()
		stack.addWidget(theme)
		about = About()
		stack.addWidget(about)
		events=Events()
		stack.addWidget(events)





	



	p = QPalette()
	gradient = QLinearGradient(0, 0, 0, 400)
	gradient.setColorAt(0.0, QColor("#64afab"))
	gradient.setColorAt(0.5, QColor("#c0d9d8"))
	gradient.setColorAt(0.1, QColor("#64afab"))
	
	p.setBrush(QPalette.Window, QBrush(gradient))
	window.setPalette(p)
	
	
	page1Button = QPushButton("")
	page1Button.setStyleSheet("background:transparent;"
								
								"background-image:url(projects1.png);"
								#"color:rgb(74, 94, 93);"
								#"font: 75 18pt;"
								#"border-width:12px;"
								#" border:5px solid rgb(255, 170, 255);"
								"border-radius:25px;"
								"max-width:50px;"
								"max-height:50px;"
								"min-width:50px;"
								"min-height:50px;")
	page1Button.setToolTip("<html><head/><body><p>Projects</p></body></html>")

	page2Button = QPushButton("")
	page2Button.setStyleSheet("background:transparent;"
								#"background-color:#4ba4e6;"
								#"color:rgb(74, 94, 93);"
								#"font: 75 18pt;"
								"background-image:url(logistics1.png);"

								#"border-width:12px;"
								#" border:5px solid rgb(255, 170, 255);"
								"border-radius:25px;"
								"max-width:50px;"
								"max-height:50px;"
								"min-width:50px;"
								"min-height:50px;")
	page2Button.setToolTip("<html><head/><body><p><span style=\" color:#000000;\"><b>Logistics</b></span></p></body></html>")
	
	page3Button = QPushButton("") 
	page3Button.setStyleSheet("background:transparent;"
								#"background-color:#4ba4e6;"
								#"color:rgb(74, 94, 93);"
								#"font: 75 18pt;"
								"background-image:url(theme1.png);"

								#"border-width:12px;"
								#" border:5px solid rgb(255, 170, 255);"
								"border-radius:25px;"
								"max-width:50px;"
								"max-height:50px;"
								"min-width:50px;"
								"min-height:50px;")
	page3Button.setToolTip("<html><head/><body><p><span style=\" color:#000000;\"><b>Theme</b></span></p></body></html>")

	page4Button = QPushButton("")
	page4Button.setStyleSheet("background:transparent;"
								#"background-color:#4ba4e6;"
								"background-image:url(about1.png);"
								#"color:rgb(74, 94, 93);"
								#"font: 75 18pt;"
								#"border-width:12px;"
								#" border:5px solid rgb(255, 170, 255);"
								"border-radius:25px;"
								"layout.setSpacing(10);"
								"max-width:50px;"
								"max-height:50px;"
								"min-width:50px;"
								"min-height:50px;")
	page5Button = QPushButton("")
	page5Button.setStyleSheet("background:transparent;"
								#"background-color:#4ba4e6;"
								"background-image:url(events1.png);"
								#"color:rgb(74, 94, 93);"
								#"font: 75 18pt;"
								#"border-width:12px;"
								#" border:5px solid rgb(255, 170, 255);"
								"border-radius:25px;"
								"layout.setSpacing(10);"
								"max-width:50px;"
								"max-height:50px;"
								"min-width:50px;"
								"min-height:50px;")
	page6Button = QPushButton("")
	page6Button.setStyleSheet("background:transparent;"
								#"background-color:#4ba4e6;"
								"background-image:url(login1.png);"
								#"color:rgb(74, 94, 93);"
								#"font: 75 18pt;"
								#"border-width:12px;"
								#" border:5px solid rgb(255, 170, 255);"
								"border-radius:25px;"
								"layout.setSpacing(10);"
								"max-width:50px;"
								"max-height:50px;"
								"min-width:50px;"
								"min-height:50px;")

								
	
	if num==1:
		page1Button.clicked.connect(stack.setPage1)
		page2Button.clicked.connect(stack.setPage2)
		page3Button.clicked.connect(stack.setPage3)
		page4Button.clicked.connect(stack.setPage4)
		page5Button.clicked.connect(stack.setPage5)
		page6Button.clicked.connect(stack.setPage6)

	if num==2:
		page1Button.clicked.connect(stack.setPage2)
		page2Button.clicked.connect(stack.setPage1)
		page3Button.clicked.connect(stack.setPage3)
		page4Button.clicked.connect(stack.setPage4)
		page5Button.clicked.connect(stack.setPage5)
		page6Button.clicked.connect(stack.setPage6)

	if num==3:
		page1Button.clicked.connect(stack.setPage3)
		page2Button.clicked.connect(stack.setPage2)
		page3Button.clicked.connect(stack.setPage1)
		page4Button.clicked.connect(stack.setPage4)
		page5Button.clicked.connect(stack.setPage5)
		page6Button.clicked.connect(stack.setPage6)

	if num==4:
		page1Button.clicked.connect(stack.setPage4)
		page2Button.clicked.connect(stack.setPage2)
		page3Button.clicked.connect(stack.setPage1)
		page4Button.clicked.connect(stack.setPage4)
		page5Button.clicked.connect(stack.setPage5)
		page6Button.clicked.connect(stack.setPage6)

	if num==5:
		page1Button.clicked.connect(stack.setPage2)
		page2Button.clicked.connect(stack.setPage3)
		page3Button.clicked.connect(stack.setPage4)
		page4Button.clicked.connect(stack.setPage5)
		page5Button.clicked.connect(stack.setPage1)
		page6Button.clicked.connect(stack.setPage6)

	if num==6:
		page1Button.clicked.connect(stack.setPage2)
		page2Button.clicked.connect(stack.setPage3)
		page3Button.clicked.connect(stack.setPage4)
		page4Button.clicked.connect(stack.setPage5)
		page5Button.clicked.connect(stack.setPage6)
		page6Button.clicked.connect(stack.setPage1)



		
	layout = QGridLayout(window)
	layout.addWidget(stack, 0, 1,6,6)
	layout.addWidget(page1Button, 0, 0)
	layout.verticalSpacing()
	layout.addWidget(page2Button, 1, 0)
	layout.addWidget(page3Button, 2, 0)
	layout.addWidget(page4Button, 3, 0)
	layout.addWidget(page5Button, 4, 0)
	layout.addWidget(page6Button, 5, 0)
	
	window.show()
	sys.exit(app.exec_())

if __name__ == "__main__":

	app = QApplication(sys.argv)
	
	window = QWidget()


	start(num)
	
	
	sys.exit(app.exec_())