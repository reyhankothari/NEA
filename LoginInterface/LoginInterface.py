import PyQt5
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QWidget
import resource
from PyQt5.uic import loadUi
import sys
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning) 


class LoginInterface(QDialog):
    def __init__(self):
        super(LoginInterface, self).__init__()
        loadUi("LoginInterface\LoginInterfaceUI.ui", self)
        self.show()
        
       


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = LoginInterface()
    app.exec_()

