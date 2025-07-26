import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QProgressBar, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt6.QtCore import Qt
from PyQt6 import uic
from PyQt6.QtGui import QPixmap, QIcon
from database import GymProductDatabase
from utils import ProductCRUD, MessageBox
class GymApp(QMainWindow):
    def __init__(self):
        super().__init__()
        global widgets 
        self.ui = uic.loadUi("gui/menu.ui",self)
        widgets = self.ui
        self.handleChangeNav(0)
        self.btnNavHome.clicked.connect(lambda: self.handleChangeNav(0))
        self.btnNavProduct.clicked.connect(lambda: self.handleChangeNav(1))
        self.btnNavAdd.clicked.connect(lambda: self.handleChangeNav(2))
        self.btnNavAI.clicked.connect(lambda: self.handleChangeNav(3))
        self.btnSetting.clicked.connect(lambda: self.handleChangeNav(4))
        
        global dtb
        self.dtb = GymProductDatabase()
        dtb = self.dtb
        self.setup_CRUDPage()
    
    def handleChangeNav(self,index):
        self.stackedWidget.setCurrentIndex(index)
        
    def setup_CRUDPage(self):
        self.dtb.load_data()
        self.show_info_tableWidget()

        self.btnAdd.clicked.connect(lambda: ProductCRUD.add(self))
        self.btnDelete.clicked.connect(lambda: ProductCRUD.delete(self))
        self.btnEdit.clicked.connect(lambda: ProductCRUD.edit(self))
        
    def show_info_tableWidget(self):
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.tableWidget.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Tên sản phẩm", "Mô tả", "Giá", "Số lượng", "Loại", "Thương hiệu", "Giảm giá", "Hình ảnh"])
        self.tableWidget.setRowCount(0)
        for product in self.dtb.product_list:
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)
            self.tableWidget.setItem(row_position, 0, QTableWidgetItem(str(product.id)))
            self.tableWidget.setItem(row_position, 1, QTableWidgetItem(product.name))
            self.tableWidget.setItem(row_position, 2, QTableWidgetItem(product.desc))
            self.tableWidget.setItem(row_position, 3, QTableWidgetItem(str(product.price)))
            self.tableWidget.setItem(row_position, 4, QTableWidgetItem(str(product.quantity)))
            self.tableWidget.setItem(row_position, 5, QTableWidgetItem(product.type))
            self.tableWidget.setItem(row_position, 6, QTableWidgetItem(product.brand))
            self.tableWidget.setItem(row_position, 7, QTableWidgetItem(str(product.discount)))
            item = QTableWidgetItem()
            item.setIcon(QIcon(QPixmap(product.image)))
            self.tableWidget.setItem(row_position, 8, item)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    with open("style.qss", "r") as file:
        app.setStyleSheet(file.read())

    window = GymApp()
    window.show()
    app.exec()