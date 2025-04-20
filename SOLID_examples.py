# 1. Single Responsibility Principle (SRP):
## Bad Example (Python):
## Python
class User:
  def __init__(self, name, email):
    self.name = name
    self.email = email

  def send_welcome_email(self):
      pass
    # Code to send a welcome email

  def update_profile(self, new_name, new_email):
    self.name = new_name
    self.email = new_email

  def reset_password(self):
      pass
    # Code to reset password logic
# Use code with caution.
# content_copy
# This User class has several responsibilities: managing user data, sending emails, and password resets. This violates SRP.

# Good Example (Python):
#
# Python
class User:
  def __init__(self, name, email):
    self.name = name
    self.email = email

class Emailer:
  def send_welcome_email(self, user):
      pass
    # Code to send a welcome email using user data

class PasswordReset:
  def reset_password(self, user):
      pass
    # Code to reset password logic for the user

# Usage Example
user = User("Alice", "alice@email.com")
emailer = Emailer()
emailer.send_welcome_email(user)
# Use code with caution.
# content_copy
# Here, we've separated user data management from email sending and password resets. This promotes cleaner and more focused classes.

# 2. Open-Closed Principle (OCP):
## Bad Example (Python):
## Python
class Shape:
  def __init__(self, type):
    self.type = type

  def get_area(self):
    if self.type == "square":
      return self.width * self.width
    else:
      raise Exception("Area calculation not implemented for this shape")
# Use code with caution.
# content_copy
# If we need to add a new shape like a circle, we'd have to modify the get_area method. This violates OCP.

# Good Example (Python):

# Python
from abc import ABC, abstractmethod

class Shape(ABC):
  @abstractmethod
  def get_area(self):
    pass

class Square(Shape):
  def __init__(self, width):
    self.width = width

  def get_area(self):
    return self.width * self.width

class Circle(Shape):
  def __init__(self, radius):
    self.radius = radius

  def get_area(self):
    return 3.14 * self.radius * self.radius

# Usage Example
square = Square(5)
circle = Circle(3)

print(square.get_area())  # Output: 25
print(circle.get_area())  # Output: 28.26
# Use code with caution.
# content_copy
# Here, we use an abstract base class Shape with an abstract get_area method. Subclasses like Square and Circle implement their specific area calculation logic. This allows adding new shapes without modifying existing code.
#
# 3. Liskov Substitution Principle (LSP):#
# Bad Example (Python)#
# Python
class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def get_area(self):
    return self.width * self.height

class Square(Rectangle):  # This violates LSP
  def __init__(self, side):
    self.width = side
    self.height = side  # Enforces a square

# Usage Example (incorrect behavior)
rectangle = Rectangle(4, 5)
square = Square(4)  # We can assign a square to a rectangle

print(rectangle.get_area())  # Output: 20
print(square.get_area())  # Output: 16 (incorrect behavior)
# Use code with caution.
# content_copy
# A square is a rectangle, but Square enforces a square by setting width and height equal in the constructor. This violates LSP because using a Square as a Rectangle would lead to unexpected behavior (area calculation).
# 4. Interface Segregation Principle (ISP):
# Bad Example (Python):

# Python
class Logger:
  def log_info(self, message):
      pass
    # Log info message

  def log_warning(self, message):
      pass
        # Log warning message

  def log_error(self, message):
      pass
    # Log error message

  def send_notification(self, message, severity):
        pass#
# Use code with caution.
# content_copy
# Sources
# info


# Dependency Inversion Principle (DIP):#
# Bad Example (Python):#
# Python
class DatabaseManager:
  def __init__(self):
    self.connection = MySQLConnection()  # Tight dependency on MySQL

  def save_user(self, user):
      pass
    # Code to save user data using MySQL connection

class User:
  def __init__(self, name, email):
    self.name = name
    self.email = email

  def save(self):
    database_manager = DatabaseManager()
    database_manager.save_user(self)  # User depends on DatabaseManager
# Use code with caution.
# content_copy
# In this example, the User class directly depends on the DatabaseManager class, which has a tight dependency on the MySQLConnection implementation. This makes it difficult to use the User class with other database implementations.

# Good Example (Python):
#
# Python
from abc import ABC, abstractmethod

class DatabaseConnection(ABC):
  @abstractmethod
  def save_user(self, user):
    pass

class MySQLConnection(DatabaseConnection):
    pass
  # Implementation for saving user data using MySQL

class User:
  def __init__(self, name, email):
    self.name = name
    self.email = email

  def save(self, database_connection):  # User depends on an abstraction (DatabaseConnection)
    database_connection.save_user(self)

# Usage Example
database_connection = MySQLConnection()
user = User("Bob", "bob@email.com")
user.save(database_connection)  # We can inject different connection types
# Use code with caution.
# content_copy
# Here, we introduce an abstract base class DatabaseConnection that defines a save_user method. The MySQLConnection class implements this interface. Now, the User class doesn't depend on the specific MySQLConnection implementation. Instead, it depends on the abstraction DatabaseConnection. This allows us to inject different database connection types during runtime, promoting loose coupling and flexibility.