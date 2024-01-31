"""roman to integer"""

class O:

    @staticmethod
    def romane(x):
        sum = 0
        st = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        x = x.upper()
        a = list(x)
        z = len(a)
        for i in range(z-1):
            if st[a[i]] < st[a[i+1]]:
                sum = sum - st[a[i]]
            else:
                sum = sum + st[a[i]]
        sum = sum + st[a[z-1]]

        print(sum)

O.romane(input("romane = "))






