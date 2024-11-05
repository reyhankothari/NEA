import PyQt5
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
import sys
import resource


class LoginInterface(QWidget):  # Define the LoginInterface class inheriting from QWidget
    def __init__(self,):  # Constructor method
        super(LoginInterface, self).__init__()  # Call the parent class constructor
        loadUi("LoginInterface\LoginInterfaceUI.ui", self)  # Load the UI from the .ui file
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # Remove the window's title bar
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # Set the window's background to transparent

        #Password Input
        self.password_input.setEchoMode(QLineEdit.Password)  # Set the password input to use password echo mode
        self.password_input.setCursorMoveStyle(Qt.VisualMoveStyle)  # Set the password input to use visual move style
        self.password_input.setClearButtonEnabled(True) # Adds a clear button to the password input

        #Username Input
        self.username_input.setCursorMoveStyle(Qt.VisualMoveStyle)  # Set the username input to use visual move style
        self.username_input.setClearButtonEnabled(True) # Adds a clear button to the username input
    
        #Signals
        self.login_button.clicked.connect(self.login) #Connect the login button to the login method when clicked


        self.show()

    def login(self):
        if self.password_input.text() and self.username_input.text():
            Username = self.username_input.text()
            Password = self.password_input.text()
            print("Username:", Username, "¦", "Password:", Password)
        else:
            self.error("Please enter a username and password")
            
  # Display the widget

    def error(self, text): #Display an error message box with the specified text
        QMessageBox.critical(self, "Error", text)

app = QApplication(sys.argv)# Create an application object with command-line arguments
LoginInterface = LoginInterface()# Create an instance of the LoginInterface class
app.exec_()# Execute the application's main loop

# self.username_input.returnPressed.connect(self.login_button.click)