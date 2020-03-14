from datetime import date


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def person_birth_year(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def isAdult(age):
        return age > 18

    def isOld(self):
        return self.age > 50


p1 = Person.person_birth_year("p1", 1995)
print(p1.isAdult(p1.age))
print(p1.isOld())
p2 = Person("p2", 16)
print(p2.isAdult(p2.age))
print(p1.isOld())

