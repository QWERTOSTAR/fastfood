# import packages
from PyQt5 import QtWidgets, uic


# create class Menu
class Menu(QtWidgets.QMainWindow):
    # instance initialization class
    def __init__(self):
        super().__init__()
        uic.loadUi('ui_files/menu.ui', self)
        # connecting buttons
        self.pushButton_7.clicked.connect(self.shwbasket7)
        self.pushButton_6.clicked.connect(self.shwbasket6)
        self.pushButton_5.clicked.connect(self.shwbasket5)
        self.pushButton_4.clicked.connect(self.shwbasket4)
        self.pushButton_3.clicked.connect(self.shwbasket3)
        self.pushButton_2.clicked.connect(self.shwbasket2)

    def shwbasket2(self):
        baskt.label_2.setText('burger')
        baskt.show()

    def shwbasket3(self):
        baskt.label_4.setText('pizza')
        baskt.show()

    def shwbasket4(self):
        baskt.label_5.setText('nuggets')
        baskt.show()

    def shwbasket5(self):
        baskt.label_6.setText('sushi')
        baskt.show()

    def shwbasket6(self):
        baskt.label_7.setText('soup')
        baskt.show()

    def shwbasket7(self):
        baskt.label_8.setText('fries')
        baskt.show()


# point of entry
if __name__ == '__main__':
    import sys
    from basket import Basket
    app = QtWidgets.QApplication(sys.argv)
    baskt = Basket()
    ex = Menu()
    ex.show()
    sys.exit(app.exec())
