# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'display.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import serial, time, datetime, struct
import sys
import random
newarray=[]
distarray=[]
data1=""
m=""
k=0
ser = serial.Serial('COM4',57600)
pack = [0xef01, 0xffffffff, 0x1]


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

class Ui_Dialog(object):
	def setupUi(self, Dialog):
		Dialog.setObjectName(_fromUtf8("Dialog"))
		Dialog.resize(400, 300)
		self.verticalLayoutWidget = QtGui.QWidget(Dialog)
		self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 281))
		self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
		self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		
		self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		self.verticalLayout.addWidget(self.pushButton)
		self.pushButton.clicked.connect(self.finger_call_main)
		
		self.pushButton1 = QtGui.QPushButton(self.verticalLayoutWidget)
		self.pushButton1.setObjectName(_fromUtf8("pushButton1"))
		self.verticalLayout.addWidget(self.pushButton1)
		self.pushButton1.clicked.connect(self.mainfuncn)
		
		self.lineEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
		self.lineEdit.setText(_fromUtf8(""))
		self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
		self.verticalLayout.addWidget(self.lineEdit)

		self.retranslateUi(Dialog)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

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

	def new(self):
	
		m=random.randrange(1,250)
		if m in distarray:
			print("hii")
			# newarray.append(m)
			self.new()
				
		else:
			print("else")
			distarray.append(m)
		id1=m
		print(id1)
		return id1
		#for x in distarray:
			#print(x)

	def search(self):
		data = [0x4, 0x1, 0x0, 0x0, 0x0, 0x5]
		self.writePacket(data)
		s = self.readpacket()
		return s[4:-1]	
	
	
	
	def finger_call_main(self):
		

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

		id=self.new()

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
		#print('Search result', r)
		if r[0] == 0:
			print('Successful')
			sys.exit(0)
		else:
			print('Unsuccessful')
		sys.exit(1)


		

	

	def retranslateUi(self, Dialog):
		Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
		self.pushButton.setText(_translate("Dialog", "PushButton", None))


if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	Dialog = QtGui.QDialog()
	ui = Ui_Dialog()
	ui.setupUi(Dialog)
	Dialog.show()
	sys.exit(app.exec_())

