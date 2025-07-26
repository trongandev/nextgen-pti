from dialog import AddDialog, EditDialog
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtWidgets import QTableWidgetItem
class MessageBox(QMessageBox):
    def __init__(self,text):
        super().__init__()
        self.setWindowTitle("Thông báo")
        self.setIcon(QMessageBox.Icon.Warning)
        self.setStyleSheet("background-color: #fefefe")
        self.setText(text)


class ProductCRUD:
        
    def add(self):
        dialog = AddDialog()
        if dialog.exec():
            inputs = dialog.return_input_fields()
            print(inputs)
            self.dtb.save_data(inputs)
            self.show_info_tableWidget()
    
    def edit(self):
        currIndex = self.ui.tableWidget.currentRow()
        item = self.ui.tableWidget.item(currIndex, 1)  
        if item:
            item_title = item.text()
            find_item = self.dtb.get_item_by_title(item_title)
            edit_dialog = EditDialog(find_item)
            if edit_dialog.exec():
                inputs = edit_dialog.return_input_fields()
                print(inputs)
                self.dtb.edit_item_from_dict(item_title, inputs)
                self.show_info_tableWidget()
        else:
            msg = MessageBox("Vui lòng chọn 1 bộ phim để chỉnh sửa")
            msg.exec()
            
    def delete(self):
        currIndex = self.ui.tableWidget.currentRow()
        item = self.ui.tableWidget.item(currIndex,1)
        if item:
            item_title = item.text()
            reply = QMessageBox.question(self, "Xác nhận xóa", f"Bạn có chắc muốn xóa bộ phim '{item_title}'?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.Yes:
                self.ui.tableWidget.removeRow(currIndex)
                self.dtb.delete_item(item_title)
                self.show_info_tableWidget()
        else:
            msg = MessageBox("Vui lòng chọn 1 bộ phim để xóa")
            msg.exec()