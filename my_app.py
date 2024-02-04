from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QFont, QDoubleValidator, QIntValidator
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)
 
from instr import *
from second_win import *
from final_win import *

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()    
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.button = QPushButton(txt_next)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text, alignment= Qt.AlignLeft)
        self.layout.addWidget(self.instruction, alignment= Qt.AlignLeft)
        self.layout.addWidget(self.button, alignment= Qt.AlignCenter)         
        self.setLayout(self.layout)
    def connects(self):
        self.button.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.tw = TestWin()
 
App = QApplication([])
MainWin = MainWin()
App.exec_()
