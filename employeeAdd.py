from PyQt6.QtWidgets import QDialog, QMessageBox

from employee import Employee
from employeeView import Ui_EmployeeView
from employees import Employees


class EmployeeAdd(QDialog):
    def __init__(self, employees, employee: Employee = None):
        super().__init__()
        self.ui = Ui_EmployeeView()
        self.ui.setupUi(self)
        self.ui.saveButton.clicked.connect(self.save)
        self.employees = employees
        self.employee = employee
        if employee is not None:
            self.ui.nameValue.setText(employee.name)
            self.ui.secondNameValue.setText(employee.surname)
            self.ui.peselValue.setText(employee.pesel)
            self.ui.typeCheckBox.setChecked(employee.contract)
            self.ui.PhoneValue.setText(employee.phoneNumber)

    def save(self):
        if self.employee is not None:
            self.employees.remove(self.employee)

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
