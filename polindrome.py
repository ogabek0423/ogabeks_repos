"""polindrome"""

def pl(x:int):
    if x//100 == x % 10:
        print(True)
    else:
        print(False)

pl(int(input("num = ")))


