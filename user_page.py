import json
from datetime import datetime
import os
import function
import models

def user_p(username, password):
    """user sahifasi"""
    print("Foydalanuvchi sahifasi")
    menu = input(f"""
    1.Kurslar ro'yxati
    2.kursga yozilish 
    3.manzillar
    4.Profil malumotlari
    5.chiqish
      """)
    if menu == '1':
        return function.kurslarf(username, password)
    elif menu == '2':
        return function.add_member(username, password)
    elif menu == '3':
        return function.maps(username, password)
    elif menu == '4':
        return function.profil(username, password)
    elif menu == '5':
        return function.logout(username, password)
    else :
        print("bunday buyruq yo'q qayta kiriting")
        return user_p(username, password)
