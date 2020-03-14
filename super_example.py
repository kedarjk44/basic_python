
class animal:
    def __init__(self, name):
        self.name = name
        print("Name of the animal is", self.name)


class dog(animal):
    def __init__(self, name, has_fur):
        super(dog, self).__init__(name)
        print("Type of the animal is dog.")
        if has_fur:
            print("%s has fur." % self.name)
        else:
            print("%s has no fur." % self.name)

    def bark(self):
        print("Barking loudly.. bow.. bow")


class bulldog(dog):
    def __init__(self, name, has_fur, is_angry):
        super(bulldog, self).__init__(name, has_fur)
        print("this is a bulldog")
        if is_angry:
            print("%s bites" % self.name)
        else:
            print("%s licks" % self.name)

    def bark(self):
        return super().bark()


# sam = dog("sam", has_fur=True)
# bob = dog("bob", has_fur=False)
bull = bulldog("bully", has_fur=True, is_angry=True)
bull.bark()
lucky = bulldog("lucky", has_fur=True, is_angry=False)
