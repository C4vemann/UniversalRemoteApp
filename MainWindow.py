import time

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QTimer, QDateTime,QTimer
from app_design import Ui_Form


class MainWindow(QMainWindow):
	def __init__(self,parent=None):
		super(MainWindow, self).__init__(parent)

		self.current_light = None

		self.timer2 = QTimer(self)
		self.timer2.timeout.connect(self.on_timeout)

		self.ui = Ui_Form()
		self.ui.setupUi(self)
		
		self.ui.tv.clicked.connect(self.tv_clicked)
		self.ui.other1.clicked.connect(self.other1_clicked)
		self.ui.other2.clicked.connect(self.other2_clicked)
		self.ui.other3.clicked.connect(self.other3_clicked)
		self.ui.other4.clicked.connect(self.other4_clicked)


		self.ui.one.clicked.connect(self.one_clicked)
		self.ui.two.clicked.connect(self.two_clicked)
		self.ui.three.clicked.connect(self.three_clicked)
		self.ui.four.clicked.connect(self.four_clicked)
		self.ui.five.clicked.connect(self.five_clicked)
		self.ui.six.clicked.connect(self.six_clicked)
		self.ui.seven.clicked.connect(self.seven_clicked)
		self.ui.eight.clicked.connect(self.eight_clicked)
		self.ui.nine.clicked.connect(self.nine_clicked)
		self.ui.zero.clicked.connect(self.zero_clicked)
		self.ui.clear.clicked.connect(self.clear_clicked)

		self.ui.home.clicked.connect(self.home_clicked)
		self.ui.settings.clicked.connect(self.settings_clicked)


		timer = QTimer(self)
		timer.timeout.connect(self.update_time)
		timer.start(1000)
		self.update_time


	def update_time(self):
		current_datetime = QDateTime.currentDateTime()
		current_time = current_datetime.toString("hh:mm:ss")
		self.ui.clock.setText(current_time)

	
	def tv_clicked(self):
		if self.current_light == self.ui.tv_light:
			self.current_light.setStyleSheet("background-color:red")
			self.current_light = None
			return
		self.ui.selection.setText("Master Bedroom")
		if self.current_light:
			self.current_light.setStyleSheet("background-color:red")

		self.current_light = self.ui.tv_light
		self.current_light.setStyleSheet("background-color:green")
		
		self.timer2.start(5000)

		self.ui.stacked_widget.setCurrentIndex(0)

		print("tv_clicked")

	def on_timeout(self):
		self.timer2.stop()

	def other1_clicked(self):
		if self.current_light == self.ui.other1_light:
			self.current_light.setStyleSheet("background-color:red")
			self.current_light = None
			return
		self.ui.selection.setText("Other 1")
		if self.current_light:
			self.current_light.setStyleSheet("background-color:red")

		self.current_light = self.ui.other1_light
		self.current_light.setStyleSheet("background-color:green")
		
		self.timer2.start(5000)
		
		self.ui.stacked_widget.setCurrentIndex(0)

		print("other1_clicked")
	def other2_clicked(self):
		if self.current_light == self.ui.other2_light:
			self.current_light.setStyleSheet("background-color:red")
			self.current_light = None
			return
		self.ui.selection.setText("Other 2")
		if self.current_light:
			self.current_light.setStyleSheet("background-color:red")

		self.current_light = self.ui.other2_light
		self.current_light.setStyleSheet("background-color:green")
		
		self.timer2.start(5000)

		self.ui.stacked_widget.setCurrentIndex(0)

		print("other2_clicked")

	def other3_clicked(self):
		if self.current_light == self.ui.other3_light:
			self.current_light.setStyleSheet("background-color:red")
			self.current_light = None
			return
		self.ui.selection.setText("Other 3")
		if self.current_light:
			self.current_light.setStyleSheet("background-color:red")

		self.current_light = self.ui.other3_light
		self.current_light.setStyleSheet("background-color:green")
		
		self.timer2.start(5000)
		
		self.ui.stacked_widget.setCurrentIndex(0)

		print("other3_clicked")
	def other4_clicked(self):
		if self.current_light == self.ui.other4_light:
			self.current_light.setStyleSheet("background-color:red")
			self.current_light = None
			return
		self.ui.selection.setText("Other 4")
		if self.current_light:
			self.current_light.setStyleSheet("background-color:red")

		self.current_light = self.ui.other4_light
		self.current_light.setStyleSheet("background-color:green")
		
		self.timer2.start(5000)
		
		self.ui.stacked_widget.setCurrentIndex(0)
		
		print("other4_clicked")


	def one_clicked(self):
		current_value = self.ui.number_screen.intValue()
		new_value = current_value * 10 + 1
		self.ui.number_screen.display(new_value)
		print("one_clicked")
	def two_clicked(self):
		current_value = self.ui.number_screen.intValue()
		new_value = current_value * 10 + 2
		self.ui.number_screen.display(new_value)
		print("two_clicked")
	def three_clicked(self):
		current_value = self.ui.number_screen.intValue()
		new_value = current_value * 10 + 3
		self.ui.number_screen.display(new_value)
		print("three_clicked")
	def four_clicked(self):
		current_value = self.ui.number_screen.intValue()
		new_value = current_value * 10 + 4
		self.ui.number_screen.display(new_value)
		print("four_clicked")
	def five_clicked(self):
		current_value = self.ui.number_screen.intValue()
		new_value = current_value * 10 + 5
		self.ui.number_screen.display(new_value)
		print("five_clicked")
	def six_clicked(self):
		current_value = self.ui.number_screen.intValue()
		new_value = current_value * 10 + 6
		self.ui.number_screen.display(new_value)
		print("six_clicked")
	def seven_clicked(self):
		current_value = self.ui.number_screen.intValue()
		new_value = current_value * 10 + 7
		self.ui.number_screen.display(new_value)
		print("seven_clicked")
	def eight_clicked(self):
		current_value = self.ui.number_screen.intValue()
		new_value = current_value * 10 + 8
		self.ui.number_screen.display(new_value)
		print("eight_clicked")
	def nine_clicked(self):
		current_value = self.ui.number_screen.intValue()
		new_value = current_value * 10 + 9
		self.ui.number_screen.display(new_value)
		print("nine_clicked")
	def zero_clicked(self):
		current_value = self.ui.number_screen.intValue()
		new_value = current_value * 10 + 0
		self.ui.number_screen.display(new_value)
		print("zero_clicked")
	def clear_clicked(self):
		current_value = self.ui.number_screen.intValue()
		self.ui.number_screen.display(current_value * 0)
		print("clear_clicked")

	def home_clicked(self):
		self.ui.stacked_widget.setCurrentIndex(1)
		self.ui.selection.setText("Main Menu")
		print("home_clicked")
	def settings_clicked(self):
		print("settings_clicked")

		