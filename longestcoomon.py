class Prefix:
    @staticmethod
    def pre():
        x = ['abcdef', 'abcde', 'abcd', 'abcdefg']
        y = list(x[0])
        a = ''
        for z in range(len(y)):
            b = a
            a += y[z]
            for i in range(len(x)):
                if a in x[i]:
                    pass
                else:
                    print(b)
                    break

Prefix.pre()



