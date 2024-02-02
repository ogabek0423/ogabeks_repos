"""polindrome"""

def pl(x):
    z = list(x)
    y = len(z)
    a=0
    for i in range(y//2):
        if z[i] == z[-(1+i)]:
            a+=1
    if a == y//2:
        print(True)
    else:
        print(False)

pl((input("num = ")))


