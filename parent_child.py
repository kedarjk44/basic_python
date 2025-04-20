class Animal:
    """
    A parent class representing animals.
    """
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")


class Dog(Animal):
    """
    A child class representing dogs, inheriting from Animal.
    """
    def __init__(self, name, breed):
        super().__init__(name)  # Call the parent class constructor
        self.breed = breed

    def bark(self):
        print(f"{self.name} the {self.breed} is barking!")


# Create an Animal instance
animal = Animal("Leo")
animal.eat()  # Output: Leo is eating.

# Create a Dog instance
dog = Dog("Charlie", "Golden Retriever")
dog.eat()  # Output: Charlie is eating. (Inherits from Animal)
dog.bark()  # Output: Charlie the Golden Retriever is barking!
