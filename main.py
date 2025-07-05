import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QProgressBar, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
from PyQt5 import uic

class GymApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("gui/menu.ui",self)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    with open("style.qss", "r") as file:
        app.setStyleSheet(file.read())

    window = GymApp()
    window.show()
    sys.exit(app.exec_())