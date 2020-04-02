class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("Age can't be negative.")

    @property
    def full_name(self):
        return f"{self.first} {self.last}"



joe = Human("Joseph", "Gutierrez", 28)
print(joe.age)
joe.age = 30
print(joe.age)