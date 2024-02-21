import json
import os
import sys
from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox, QMainWindow

import employees
from employee import EmployeeEncoder
from employeeAdd import EmployeeAdd
from employees import Employees
from menu import Ui_Menu


class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Menu()
        self.ui.setupUi(self)
        self.show()
        self.ui.add.clicked.connect(self.add)
        self.ui.save.clicked.connect(self.save)
        self.ui.load.clicked.connect(self.load)
        self.ui.edit.clicked.connect(self.edit)
        self.ui.search.clicked.connect(self.search)
        self.employees = Employees()

    def add(self):
        w = EmployeeAdd(self.employees)
        w.show()
        w.exec()
        self.ui.comboBox.clear()
        self.ui.comboBox.addItems(self.employees.get_list())

    def save(self):
        if self.employees.list == []:
            QMessageBox.about(self, "blad", "nie ma pracownikow w liscie")
        else:
            with open('employees.json', 'w') as file:
                json.dump(self.employees.to_json(), file, cls=EmployeeEncoder, indent=2)
            QMessageBox.about(self, "Zapis", "pracownicy zapisani do pliku")

    def load(self):
        if not os.path.exists("employees.json"):
            QMessageBox.about(self, "Błąd", "Plik nie istnieje")
        else:
            if self.employees.load_list() == []:
                QMessageBox.about(self, "Wczytanie", "brak pracowników w pliku")
            else:
                if self.ui.comboBox.count() == 0:
                    self.ui.comboBox.addItems(self.employees.load_list())
                    QMessageBox.about(self, "Wczytanie", "Wczytano dane z pliku")
                else:
                    QMessageBox.about(self, "Wczytanie", "dane z pliku zostały już wczytane")

    def edit(self):
        emp_str = self.ui.comboBox.currentText()
        pesel = emp_str[:11]
        emp = self.employees.get(pesel=pesel)[0]
        w = EmployeeAdd(self.employees, emp)
        w.show()
        w.exec()

    def search(self):
        pesel = self.ui.pesel.text()
        for i in range(self.ui.comboBox.count()):
            if self.ui.comboBox.itemText(i)[:11].startswith(pesel):
                self.ui.comboBox.setCurrentIndex(i)
                return





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    window.setWindowTitle('Pracownicy')
    window.show()
    sys.exit(app.exec())
