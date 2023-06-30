# import packages
from PyQt5 import QtWidgets, uic


# create classes
class Basket(QtWidgets.QMainWindow):
    # instance initialization class

    def __init__(self):
        super().__init__()
        uic.loadUi('ui_files/basket.ui', self)
    # I create function that delete anything
        self.pushButton_6.clicked.connect(self.delt)
    # I create a function that removes the desired food
        self.pushButton_7.clicked.connect(self.delt_food)
    # create a function that buys food
        self.pushButton_8.clicked.connect(self.buy_food)

    def delt(self):
        self.label_2.setText('')
        self.label_4.setText('')
        self.label_5.setText('')
        self.label_6.setText('')
        self.label_7.setText('')
        self.label_8.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit_3.setText('')
        self.lineEdit_4.setText('')
        self.lineEdit_5.setText('')
        self.lineEdit_6.setText('')
        self.lineEdit_7.setText('')

    def delt_food(self):
        if self.lineEdit.text() == 'burger':
            self.label_2.setText('')
        if self.lineEdit.text() == 'pizza':
            self.label_4.setText('')
        if self.lineEdit.text() == 'nuggets':
            self.label_5.setText('')
        if self.lineEdit.text() == 'sushi':
            self.label_6.setText('')
        if self.lineEdit.text() == 'soup':
            self.label_7.setText('')
        if self.lineEdit.text() == 'fries':
            self.label_8.setText('')

    def buy_food(self):
        self.lineEdit_8.setText('delivery will arrive in 10 minutes')
        self.label_2.setText('')
        self.label_4.setText('')
        self.label_5.setText('')
        self.label_6.setText('')
        self.label_7.setText('')
        self.label_8.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit_3.setText('')
        self.lineEdit_4.setText('')
        self.lineEdit_5.setText('')
        self.lineEdit_6.setText('')
        self.lineEdit_7.setText('')
