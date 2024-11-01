import PyQt5
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.uic import loadUi
import sys
import resource


class LoginInterface(QWidget):  # Define the LoginInterface class inheriting from QWidget
    def __init__(self,):  # Constructor method
        super(LoginInterface, self).__init__()  # Call the parent class constructor
        loadUi("LoginInterface\LoginInterfaceUI.ui", self)  # Load the UI from the .ui file
        self.show()  # Display the widget
    

app = QApplication(sys.argv)# Create an application object with command-line arguments
LoginInterface = LoginInterface()# Create an instance of the LoginInterface class
app.exec_()# Execute the application's main loop
