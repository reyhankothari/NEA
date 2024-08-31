import sys
import PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QGraphicsPixmapItem
from PyQt5.uic import loadUi

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('C:/Users/Rey10/Desktop/NEA/UserInterface/Login Interface/Test.ui', self)
        


    
       
    
app = QApplication(sys.argv)

window = MainWindow()   
window.show()
app.exec_()

