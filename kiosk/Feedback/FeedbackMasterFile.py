import feedback
import feedbackLogin

from feedback import Ui_MainWindow
from feedbackLogin import Ui_MainWindow2

from PyQt4 import QtGui
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import pymysql

DatabaseName="noname"

class FeedbackMainWindow (QtGui.QMainWindow, feedbackLogin.Ui_MainWindow2):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.setupUi(self)

		self.pushButton.clicked.connect(self.loadFeedbackAndQuery)
		self.window2 = None

	def loadFeedbackAndQuery (self):
		#SQL QUERY PART ONLY.
		# Open database connection
		db = pymysql.connect("localhost","root","","testsept" )

		# prepare a cursor object using cursor() method
		cursor = db.cursor()

		nameInput = self.plainTextEdit.toPlainText()
		try:
			# Execute the SQL command
				cursor.execute("""SELECT name from registerForm""")
				# Commit your changes in the database
				#db.commit()
				for (name) in cursor:
					changedName = ''.join(e for e in format(name) if e.isalnum())
					if (changedName==nameInput):
						print ("Login successful")
						globals()["DatabaseName"] = nameInput
						if self.window2 == None:
							self.window2 = FeedbackMainFile() 
							print ("Command passsed")
						self.window2.show()
						break
					else:
						print ("Failed!")

				cursor.close()

		except:
			# Rollback in case there is any error
			db.rollback()

			# disconnect from server
			db.close()

			#SQL QUERY PART HAS ENDED

class FeedbackMainFile (QtGui.QMainWindow, feedback.Ui_MainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.setupUi(self)
		self.setUserData(self)

	def printingFeedbackUserDetail(self):
		# Open database connection
		db = pymysql.connect("localhost","root","","testsept" )
		# prepare a cursor object using cursor() method
		cursor = db.cursor()
		#fetching the input and storing in the variables
		nameInput=self.plainTextEdit.toPlainText()
		try:
			# Execute the SQL command
			cursor.execute("""SELECT name from registerForm """)

			if (globals()["DatabaseName"]=="q"):
				print (globals()["DatabaseName"])
				self.plainTextEdit.setPlainText("q")
				self.plainTextEdit_2.setPlainText("q")
				self.plainTextEdit_3.setPlainText("q")
				self.plainTextEdit_4.setPlainText("q")
			cursor.close()
		except:
			# Rollback in case there is any error
			db.rollback()

			# disconnect from server
			db.close()


if  __name__ == '__main__':

	import sys
	app = QtGui.QApplication(sys.argv)
	window = FeedbackMainWindow()
	window.show()
	sys.exit(app.exec_())
