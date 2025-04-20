class employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age_from_name(self, name):
        if name == self.name:
            return self.age
        return False

    def get_name_from_age(self, age):
        if age == self.age:
            return self.name
        return False


class it_employee(employee):
    def __init__(self, name, age, skill):
        super().__init__(name, age)
        super().get_name_from_age(age)
        # super().get_age_from_name(name)
        self.skill = skill

    def print_skill(self):
        print(self.skill)

    def get_name_from_age(self, age):
        return "super returns " + super().get_name_from_age(age)

# empl1 = employee("Kedar", 39)
# print(empl1.get_age_from_name("Kedar"))
# print(empl1.get_name_from_age(39))


empl2 = it_employee("Kedar", 39, "Python")
empl2.print_skill()
print(empl2.get_name_from_age(39))
print(empl2.get_age_from_name("Kedar"))
print(empl2.get_age_from_name("Riddhi"))
