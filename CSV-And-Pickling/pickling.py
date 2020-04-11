import pickle

class Animal:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, breed)
        self.toy = toy

    def play(self):
        return f"{self.name} is playing with {self.toy}."

wong = Cat("Wong", "Tuxie", "String")

with open("cat.pickle", "wb") as file:
    pickle.dump(wong, file)

with open("cat.pickle", "rb") as file:
    zombie_wong = pickle.load(file)

print(zombie_wong)