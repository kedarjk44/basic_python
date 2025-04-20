# Method Overloading (Python doesn't have true overloading, so we simulate it)

class Calculator:
    def add(self, a, b=None, c=None):
        if b is not None and c is not None:
            return a + b + c
        elif b is not None:
            return a + b
        else:
            return a

calc = Calculator()
print(calc.add(5))
print(calc.add(5, 10))
print(calc.add(5, 10, 15))

# Abstraction

from abc import ABC, abstractmethod

class Shape(ABC):  # ABC = Abstract Base Class
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

circle = Circle(5)
rectangle = Rectangle(4, 6)

print("Circle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter())
print("Rectangle Area:", rectangle.area())
print("Rectangle Perimeter:", rectangle.perimeter())

# Multiple Inheritance

class Engine:
    def start(self):
        print("Engine started")

    def stop(self):
        print("Engine stopped")

class ElectricMotor:
    def charge(self):
        print("Electric motor charging")

    def discharge(self):
        print("Electric motor discharging")

class HybridCar(Engine, ElectricMotor):
    def drive(self):
        print("Hybrid car driving")

hybrid_car = HybridCar()
hybrid_car.start()
hybrid_car.charge()
hybrid_car.drive()
hybrid_car.discharge()
hybrid_car.stop()

# DRY: Avoid redundancy. - don't repeat yourself
# KISS: Keep it simple, stupid
# YAGNI: Don't implement unnecessary features. - you ain't gonna need it
# SOLID: Create robust and maintainable object-oriented designs.