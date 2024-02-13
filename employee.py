import json
from typing import Any


class Employee:

    next_id = 0

    def __init__(self, surname: str, name: str, phoneNumber: str, pesel: str, contract: bool):
        self.id = Employee.next_id
        Employee.next_id += 1
        self.name = name
        self.surname = surname
        self.phoneNumber = phoneNumber
        self.contract = contract
        if len(pesel) == 11 and self.validatePesel(pesel):
            self.pesel = pesel
        else:
            raise ValueError

    def __str__(self) -> str:
        return f'{self.pesel}, {self.name} {self.surname}'

    def validatePesel(self, pesel: str):
        sum = 0
        weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
        for i in range(10):
            x = weights[i] * int(pesel[i])
            sum += x
        controlNumber = 0
        sum = sum % 10
        if sum == 0:
            controlNumber = sum
        else:
            controlNumber = 10 - sum

        if controlNumber != int(pesel[10]):
            return False
        else:
            return True


class EmployeeEncoder(json.JSONEncoder):
    def default(self, o) -> dict:
        if isinstance(o, Employee):
            return {'id': o.id,
                    'name': o.name,
                    'surname': o.surname,
                    'phoneNumber': o.phoneNumber,
                    'pesel': o.pesel,
                    'contract': o.contract}
        return super().default(o)