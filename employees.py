from employee import Employee, EmployeeEncoder
import json


class Employees:

    def __init__(self):
        self.list = []
    
    def to_json(self):
        return [EmployeeEncoder().default(emp) for emp in self.list]
    
    def save_list(self):
        with open('employees.json', 'w') as file:
            json.dump(self.to_json(), file)

    def load_list(self):
        with open('employees.json', 'r') as file:
            data = json.load(file)
        self.list = []
        for emp in data:
            self.add(Employee(emp['surname'], emp['name'], emp['phoneNumber'], emp['pesel'], emp['contract']))
        return [f"{emp.pesel} {emp.name} {emp.surname}" for emp in self.list]
                
    def add(self, emp: Employee):
        self.list.append(emp)

    def remove(self, emp: Employee):
        self.list.remove(emp)


    def get(self, id=None, name=None, surname=None, pesel=None):
        result = []
        for emp in self.list:
            if emp.id == id:
                result.append(emp)
            elif emp.name == name:
                result.append(emp)
            elif emp.surname == surname:
                result.append(emp)
            elif emp.pesel == pesel:
                result.append(emp)

        return result

    def get_list(self) -> list:
        return [e.__str__() for e in self.list]
