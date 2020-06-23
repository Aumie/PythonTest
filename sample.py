class Math :
    def add(self, a, b):
        return a+b

    def max(self, a, b):
        return a if a>b else b

    def getOddNumber(self,limit):
        return [i for i in range(limit) if i % 2 != 0]


print('created')