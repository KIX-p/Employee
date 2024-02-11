from PyQt6.QtWidgets import QDialog, QMessageBox

from employee import Employee
from employeeView import Ui_EmployeeView


class EmployeeAdd(QDialog):
    def __init__(self, employees):
        super().__init__()
        self.ui = Ui_EmployeeView()
        self.ui.setupUi(self)
        self.ui.saveButton.clicked.connect(self.save)
        self.employees = employees

    def save(self):
        name = self.ui.nameValue.text()
        secondName = self.ui.secondNameValue.text()
        pesel = self.ui.peselValue.text()
        contract = self.ui.typeCheckBox.isChecked()
        phone = self.ui.PhoneValue.text()
        try:
            emp = Employee(secondName, name, phone, pesel, contract)
            self.employees.add(emp)
            self.close()
        except ValueError:
            messageBox = QMessageBox()
            messageBox.setText("Błędny numer pesel")
            messageBox.setWindowTitle("Błąd")
            messageBox.exec()
