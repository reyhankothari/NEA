import PyQt5
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QMessageBox, QMainWindow, QHeaderView
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
import sys
import sqlite3
import bcrypt

sys.path.insert(0, r'C:\Users\Rey10\Desktop\Computer Science NEA\NEA')

class homePage(QMainWindow):  # Define the LoginInterface class inheriting from QWidget
    def __init__(self):  # Constructor method
        
        super(homePage, self).__init__()  # Call the parent class constructor
        loadUi('HomePage\HomePageUI.ui', self)  # Load the UI from the .ui file

        self.ordermenu_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.predictionmenu_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(5))
        self.productinformationmenu_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.reportsmenu_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.salesmenu_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.settingsmenu_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(6))
        self.sign_out_button.clicked.connect(lambda: self.close())

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)# Create an application object with command-line arguments
    LoginInterface = homePage()# Create an instance of the home menu
    app.exec_()# Execute the application's main loop