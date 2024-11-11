import PyQt5
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
import sys
import resource
import sqlite3
import bcrypt
import sys

sys.path.insert(0, r'C:\Users\Rey10\Desktop\Computer Science NEA\NEA')
from HomePage.test import testInterface


class LoginInterface(QWidget):  # Define the LoginInterface class inheriting from QWidget
    def __init__(self,):  # Constructor method
        super(LoginInterface, self).__init__()  # Call the parent class constructor
        loadUi("LoginInterface\LoginInterfaceUI.ui", self)  # Load the UI from the .ui file
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # Remove the window's title bar
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # Set the window's background to transparent

        self.connect = sqlite3.connect('database.db')
        self.cursor = self.connect.cursor()

        #Password Input
        self.password_input.setEchoMode(QLineEdit.Password)  # Set the password input to use password echo mode
        self.password_input.setCursorMoveStyle(Qt.VisualMoveStyle)  # Set the password input to use visual move style
        self.password_input.setClearButtonEnabled(True) # Adds a clear button to the password input

        #Username Input
        self.username_input.setCursorMoveStyle(Qt.VisualMoveStyle)  # Set the username input to use visual move style
        self.username_input.setClearButtonEnabled(True) # Adds a clear button to the username input
    
        #Signals
        self.login_result = self.login_button.clicked.connect(self.login) #Connect the login button to the login method when clicked
        # Now self.login_result is the return value of the login function
        self.username_input.returnPressed.connect(self.login_button.click)
        self.password_input.returnPressed.connect(self.login_button.click) #Connect the login button to the login method when clicked
       
        self.show()

    def login(self):
        valid = self.verify() # Check if the credentials are valid
        if valid:
            self.close() # Close the login interface
            self.test = testInterface()  # Create an instance of the temporary class
            self.test.show()  # Show the instance of the temporary class
            
        


    def verify(self):
        #Check if the username and password are present
        username_present = bool(self.username_input.text()) 
        password_present = bool(self.password_input.text())  
        if username_present and password_present:
            #Print the username and password if both are present
            username = self.username_input.text()  # Get the username from the username input
            password = (self.password_input.text()).encode('utf-8')  # Get the password from the password input and encode it
            self.cursor.execute("SELECT password_hash FROM staff WHERE username = ?", (username))  # Execute an SQL query to get the hashed password from the database
            result = self.cursor.fetchone()  # Fetch the result of the query
            if result is None:
                self.error("Invalid credentials")
                return False  # Show an error message if the username is not found
            else:
                password_hash = (result[0])  # Get the hashed password from the result
                check = bcrypt.checkpw(password,password_hash)  # Check if the hashed password matches the one in the database
                if check:
                    return True  # Return True if the credentials are valid
                else:
                    # Show an error message if the credentials are invalid
                    self.error("Invalid credentials")  
                    return False  
        else:
            #Show an error message if both are not present
            self.error("Username/Password empty")  
            return False

    #Display an error message box with the specified text
    def error(self, text): 
        QMessageBox.critical(self, "Error", text)

app = QApplication(sys.argv)# Create an application object with command-line arguments
LoginInterface = LoginInterface()# Create an instance of the LoginInterface class
app.exec_()# Execute the application's main loop

