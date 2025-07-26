from PyQt6.QtWidgets import QDialog,QFileDialog
from PyQt6 import uic
from PyQt6.QtCore import QDir
from PyQt6.QtGui import QPixmap
import os
from database import Product
class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        global widget
        self.ui = uic.loadUi("gui/dialog.ui", self)
        widget = self.ui
        self.ui.btnImage.clicked.connect(lambda: self._browse_files())
        self.dir = QDir(os.getcwd())
    
    def _browse_files(self):
        fname = QFileDialog.getOpenFileName(self, "Open file", "./images")
        self.ui.btnImage.setText(str(fname[0]))
        self.ui.lbImage.setPixmap(QPixmap(fname[0]))
        return fname
    
    def return_input_fields(self):
        return {
            "name": self.ui.txtName.text(),
            "desc": self.ui.txtDesc.toPlainText(),
            "type": self.ui.cbType.currentText(),
            "price": self.ui.txtPrice.text(),
            "quantity": self.ui.txtQuantity.text(),
            "discount": self.ui.txtDiscount.text(),
            "brand": self.ui.txtBrand.text(),
            "image": self.dir.relativeFilePath(self.ui.btnImage.text()),
        }
        
class AddDialog(Dialog):
    def __init__(self):
        super().__init__()
        widget.lbTitle.setText("Thêm sản phẩm mới")
        
class EditDialog(Dialog):
    def __init__(self,edit_item: Product):
        super().__init__()
        widget.lbTitle.setText("Cập nhật thông tin sản phẩm")
        self.ui.txtName.setText(edit_item.name)
        self.ui.txtDesc.setPlainText(edit_item.desc)
        self.ui.txtPrice.setText(str(edit_item.price))
        self.ui.txtQuantity.setText(str(edit_item.quantity))
        self.ui.txtDiscount.setText(str(edit_item.discount))
        self.ui.txtBrand.setText(edit_item.brand if edit_item.brand else "")
        self.ui.cbType.setCurrentText(edit_item.type)
        self.ui.btnImage.setText(self.dir.relativeFilePath(edit_item.image))
        self.ui.lbImage.setPixmap(QPixmap(edit_item.image))
        