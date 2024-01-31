import json
import function
import admin_page
import user_page

def main():
    """login va parol kiritish"""

    username = input("username: ")
    password = input("password: ")

    with open("users.json", "r") as file:
        data = json.load(file)
        for i in data["users"]:
            if i["username"] == username and i["password"] == password:
                if i["status"] == 1:
                    return admin_page.admin_p(username, password)
                else :
                    return user_page.user_p(username, password)
        print("parol yoki foydalanuvhi nomi xato")
        return main()

if  __name__ == "__main__":
      main()