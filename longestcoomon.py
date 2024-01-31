class Prefix:
    @staticmethod
    def pre():
        x = ['ogabekjon', 'ogabek', 'ogash']
        y = list(x[0])
        a = ''
        for z in range(len(y)):
            b = a
            a += y[z]
            if a in x[0] and a in x[1] and a in x[2]:
                pass
            else:
                print(b)
                break

Prefix.pre()



