from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtUiTools import QUiLoader
import operator

import click

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.ui = loader.load("cal.ui", None)
        self.ui.show()
        self.ui.one_btn.clicked.connect(self.show_1)
        self.ui.two_btn.clicked.connect(self.show_2)
        self.ui.three_btn.clicked.connect(self.show_3)
        self.ui.four_btn.clicked.connect(self.show_4)
        self.ui.five_btn.clicked.connect(self.show_5)
        self.ui.six_btn.clicked.connect(self.show_6)
        self.ui.seven_btn.clicked.connect(self.show_7)
        self.ui.eight_btn.clicked.connect(self.show_8)
        self.ui.nine_btn.clicked.connect(self.show_9)
        self.ui.zero_btn.clicked.connect(self.show_0)
        self.ui.plus_btn.clicked.connect(self.show_plus)
        self.ui.minus_btn.clicked.connect(self.show_minus)
        self.ui.division_btn.clicked.connect(self.show_division)
        self.ui.multiply_btn.clicked.connect(self.show_multiply)
        self.ui.equal_btn.clicked.connect(self.show_equal)
        self.ui.c_btn.clicked.connect(self.show_c)

    def show_1(self):
        if self.ui.result_label.text() == '0':
            self.ui.result_label.setText('1')
        else: self.ui.result_label.setText(self.ui.result_label.text() + '1')

    def show_2(self):
        if self.ui.result_label.text() == '0':
            self.ui.result_label.setText('2')
        else: self.ui.result_label.setText(self.ui.result_label.text() + '2')

    def show_3(self):
        if self.ui.result_label.text() == '0':
            self.ui.result_label.setText('3')
        else: self.ui.result_label.setText(self.ui.result_label.text() + '3')

    def show_4(self):
        if self.ui.result_label.text() == '0':
            self.ui.result_label.setText('4')
        else: self.ui.result_label.setText(self.ui.result_label.text() + '4')
    
    def show_5(self):
        if self.ui.result_label.text() == '0':
            self.ui.result_label.setText('5')
        else: self.ui.result_label.setText(self.ui.result_label.text() + '5')
    
    def show_6(self):
        if self.ui.result_label.text() == '0':
            self.ui.result_label.setText('6')
        else: self.ui.result_label.setText(self.ui.result_label.text() + '6')
    
    def show_7(self):
        if self.ui.result_label.text() == '0':
            self.ui.result_label.setText('7')
        else: self.ui.result_label.setText(self.ui.result_label.text() + '7')
    
    def show_8(self):
        if self.ui.result_label.text() == '0':
            self.ui.result_label.setText('8')
        else: self.ui.result_label.setText(self.ui.result_label.text() + '8')
    
    def show_9(self):
        if self.ui.result_label.text() == '0':
            self.ui.result_label.setText('9')
        else: self.ui.result_label.setText(self.ui.result_label.text() + '9')
    
    def show_0(self):
        if self.ui.result_label.text() == '0':
            self.ui.result_label.setText('0')
        else: self.ui.result_label.setText(self.ui.result_label.text() + '0')
    
    def show_plus(self):
            self.plusNum1 = int(self.ui.result_label.text())
            self.ui.result_label.setText('0')
    
    def show_minus(self):
            self.minusNum1 = int(self.ui.result_label.text())
            self.ui.result_label.setText('0')
    
    def show_division(self):
            self.divisionNum1 = int(self.ui.result_label.text())
            self.ui.result_label.setText('0')
    
    def show_multiply(self):
            self.multiplyNum1 = int(self.ui.result_label.text())
            self.ui.result_label.setText('0')
    
    def show_equal(self):
        result = 0
        if self.plusNum1 != 0:
            self.plusNum2 = int(self.ui.result_label.text())
            result = self.plusNum1 + self.plusNum2
            self.ui.result_label.setText(str(result))
            self.plusNum1 = 0
        elif self.minusNum1 != 0:
            self.minusNum2 = int(self.ui.result_label.text())
            result = self.minusNum1 - self.minusNum2
            self.ui.result_label.setText(str(result))
            self.minusNum1 = 0
        elif self.divisionNum1 != 0:
            self.divisionNum2 = int(self.ui.result_label.text())
            result = self.divisionNum1 / self.divisionNum2
            self.ui.result_label.setText(str(result))
            self.divisionNum1 = 0
        elif self.multiplyNum1 != 0:
            self.multiplyNum2 = int(self.ui.result_label.text())
            result = self.multiplyNum1 * self.multiplyNum2
            self.ui.result_label.setText(str(result))
            self.multiplyNum1 = 0

    def show_c(self):
        self.ui.result_label.setText('0')

app = QApplication([])
my_calculator = Calculator()
app.exec()