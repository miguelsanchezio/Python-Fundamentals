len('asdasdas')
# 8

len('hi')
# 2

class SpecialList:
    def __init__(self, data):
        self.__data = data

    def __len__(self):
        return 50

l1 = SpecialList([1, 40, 30, 100])
l2 = SpecialList([])

print(len(l1))
print(len(l2))