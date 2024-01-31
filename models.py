import json
from datetime import datetime
class Courses:
    def __init__(self, name, description, modules_count, price, active_students, create_date=None):
        self.name = name.lower()
        self.description = description
        self.__modules_count = modules_count
        self.price = price
        self.__active_students = active_students
        self.__create_date = datetime.today()

    def get_modules_count(self):
            return self.__modules_count

    def save(self):
        new_course = {
            "name": self.name,
            "description": self.description,
            "modules_count": self.__modules_count,
            "price": self.price,
            "active_students": self.__active_students,
            "create_date": f"{datetime.today()}",

        }
        with open("kurs.json") as file:
            data = json.load(file)
            data['course'].append(new_course)
        with open("kurs.json", "w") as f:
            json.dump(data, f, indent=6)
            print("muvaffaqiyatli qo'shildi")

    def __str__(self):
        return f"{self.name}"

class User:
    def __init__(self, firstname, lastname, username, password, status, balance):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
        self.status = status
        self.balance = balance

    def get_balance(self):
        return self.balance

    def save(self):
        new_user = {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "username": self.username,
            "password": self.password,
            "status": self.status,
            "balance": self.balance,

        }
        with open("users.json", "r") as file:
            data = json.load(file)
        data["users"].append(new_user)
        with open("users.json", "w") as f:
            json.dump(data, f, indent=6)
        print("muvaffaqiyatli qo'shildi")

    def __str__(self):
        return f"{self.firstname}"













