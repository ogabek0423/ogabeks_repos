import json
import os
from mainproject import main
import admin_page
import user_page
import models


def users(username, password):

    """userlarni korish"""

    print("Sayt foydalanuvchilari :")
    with open("users.json", "r") as file:
        data = json.load(file)
        for i in data["users"]:
            print(i["firstname"], i["lastname"])

    back = input("Ortga qaytish: (back)")
    while back != "back":
        os.system("color 6")
        print("Bunday buyruq mavjud emas namunaga etibor bering")
        back = input("Orqaga qaytish: (back)")
    if back == "back":
        os.system("color 3")
        os.system("cls")
        return admin_page.admin_p(username, password)

def kurslara(username, password):

    """admin uchun kurslar royxati"""

    with open("kurs.json", 'r') as file:
        data = json.load(file)
        print("Kurslar ro'yxati: ")
        for course in data['course']:
            print(f"""
                name: {course['name']}
                izoh: {course['description']}
                modullar: {course['modules_count']}
                narxi: {course['price']}
                talabalar: {course['active_students']}
                yaratildi: {course['create_date']}
                    """)
    back = input("Ortga qaytish: (back)")
    while back != "back":
        os.system("color 6")
        print("Bunday buyruq mavjud emas namunaga etibor bering")
        back = input("Orqaga qaytish: (back)")
    if back == "back":
        os.system("color 3")
        os.system("cls")
        return admin_page.admin_p(username, password)


def kurslarf(username, password):

    """user uchun kurslar"""

    with open("kurs.json", 'r') as file:
        data = json.load(file)
        print("   Kurslar ro'yxati: ")
        for course in data['course']:
            print(f"name: {course['name']}\nizoh: {course['description']}\nmodullar: {course['modules_count']}\nnarxi: {course['price']}\nyaratildi: {course['create_date']}\n\n")
    back = input("Ortga qaytish: (back)")
    while back != "back":
        os.system("color 6")
        print("Bunday buyruq mavjud emas namunaga etibor bering")
        back = input("Orqaga qaytish: (back)")
    if back == "back":
        os.system("color 3")
        os.system("cls")
        return user_page.user_p(username, password)


def add_kurs(username, password):
    """yangi kurs qoshish"""

    l = [username, password]
    name = input("nomi:")
    name = name.lower()

    with open("kurs.json", 'r') as file:
        data = json.load(file)

    for i in data['course']:
        if i["name"] == name:
            print(i)
            # print("bunday kurs mavjud -")
            # return add_kurs(username, password)
    # description = input("izohi:")
    # modules_count = input("modullar:")
    # price = int(input("narxi:"))
    # active_students = 0
    # curs = models.Courses(name, description, modules_count, price, active_students)
    # curs.save()
    back = input("Ortga qaytish: (back)")

    while back != "back":
        os.system("color 6")
        print("Bunday buyruq mavjud emas namunaga etibor bering")
        back = input("Orqaga qaytish: (back)")

    if back == "back":
        os.system("color 3")
        os.system("cls")
        return admin_page.admin_p(username, password)



def add_member(username, password):
    """kursga yozilish"""

    with open("kurs.json", "r") as f:
        dat = json.load(f)
        print("kurslar royxati:")
    z = dat['course']
    for i in range(len(dat['course'])):
        print(1+i, z[i]["name"], ":", z[i]["price"])

    with open("users.json", "r") as file:
        data = json.load(file)

        for i in data["users"]:

            if i["username"] == username and i["password"] == password:
                x = int(i["balance"])
                print("hisobingizda:", x)

    nom = input("kurs nomini kiriting:")

    for i in range(len(dat['course'])):

        if dat['course'][i]["name"] == nom.lower():
            x = x- int(dat['course'][i]["price"])

            if x >= 0:
                dat['course'][i]["active_students"] = int(dat['course'][i]["active_students"]) + 1
                print("kursga qoshildingiz")

            elif x < 0:
                print("hisobingizda mablag' kam")

    with open("kurs.json", "w") as file:
        json.dump(dat, file, indent=6)

    with open("users.json", "r") as file:
        data = json.load(file)

        for i in data["users"]:

            if i["username"] == username and i["password"] == password:
                if x>0:
                    i["balance"] = x

    with open("users.json", "w") as file:
        json.dump(data, file, indent=6)
    back = input("Ortga qaytish: (back)")

    while back != "back":
        os.system("color 6")
        print("Bunday buyruq mavjud emas namunaga etibor bering")
        back = input("Orqaga qaytish: (back)")

    if back == "back":
        os.system("color 3")
        os.system("cls")
        return user_page.user_p(username, password)

def add_user():
    firstname = input("ismi:")
    lastname = input("familiyasi:")
    username = input("username:")
    password = input("paroli:")
    status = int(input("status:"))
    balance = int(input("mablag'i:"))
    z = models.User(firstname, lastname, username, password, status, balance)
    z.save()

    back = input("Ortga qaytish: (back)")

    while back != "back":
        os.system("color 6")
        print("Bunday buyruq mavjud emas namunaga etibor bering")
        back = input("Orqaga qaytish: (back)")

    if back == "back":
        os.system("color 3")
        os.system("cls")
        return admin_page.admin_p(username, password)

def profil(username, password):

    """profil malumotlarini korish"""

    print("Profil malumotlari")

    with open("users.json", "r") as file:
        data = json.load(file)
        for i in data["users"]:
            if i["username"] == username and i["password"] == str(password):
                print(f"ismi : {i['firstname']} \nfamiliyasi : {i['lastname']} \nusername : {i['username']} \npassword : {i['password']}\nmablagi={i['balance']}")
    back = input("Ortga qaytish: (back)")
    while back != "back":
        os.system("color 6")
        print("Bunday buyruq mavjud emas namunaga etibor bering")
        back = input("Orqaga qaytish: (back)")
    if back == "back":
        os.system("color 3")
        os.system("cls")
        with open("users.json", "r") as file:
            data = json.load(file)
            for i in data["users"]:
                if i["username"] == username and i["password"] == password:
                    if i["status"] == 1:
                        return admin_page.admin_p(username, password)
                    else:
                        return user_page.user_p(username, password)


def maps(username, password):

    """filiallar joylashuvi"""

    with open("map.json", "r") as fl:
        z = json.load(fl)
        for i in z["filiallar"]:
            print(i["name"], "filiali\njoylashuvi:", i["location"])

    back = input("Ortga qaytish: (back)")
    while back != "back":
        os.system("color 6")
        print("Bunday buyruq mavjud emas namunaga etibor bering")
        back = input("Orqaga qaytish: (back)")
    if back == "back":
        os.system("color 3")
        os.system("cls")
        return user_page.user_p(username, password)

def logout(username, password):
    """akkountdan chiqish"""
    username = False
    password = False
    # print(username, password)
    return main()

