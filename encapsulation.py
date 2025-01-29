# Encapsulation
"""
Encapsulation is a concept in object-oriented programming (OOP) that binds together the data and
the methods that manipulate that data, and keeps both safe from outside interference and misuse.
In simpler terms, encapsulation is a mechanism of bundling data and methods that operate on that
data within a single unit.
Encapsulation is used to hide the internal state of an object from the outside world and only expose 
the necessary information through public methods.
Encapsulation is achieved by using access modifiers such as public, private, and protected.
Public access modifier is used to access the data and methods from anywhere in the program.
Private access modifier is used to access the data and methods only within the same class.
Protected access modifier is used to access the data and methods within the same class and its
subclasses.
Encapsulation is used to achieve data hiding, abstraction, and code reusability.
Encapsulation is a fundamental concept in object-oriented programming (OOP) and is used in
various programming languages such as Java, C++, Python, etc.
Encapsulation is used to improve the security and maintainability of the code.
Encapsulation is used to reduce the complexity of the code and make it more readable.
Encapsulation is used to improve the performance of the code by reducing the number of
variables and methods.
Encapsulation is used to improve the reusability of the code by making it more modular.
Encapsulation is used to improve the scalability of the code by making it more flexible.
Encapsulation is used to improve the maintainability of the code by making it more modular.
Encapsulation is used to improve the security of the code by hiding the internal state of the
object.
"""


"""
Public Members
Public members are accessible from anywhere, both inside and outside the class. These are the default members in Python.
"""
class Public:
    def __init__(self):
        self.name = "Sukhi"  # Public attribute

    def display_name(self):
        print(self.name)  # Public method

obj = Public()
obj.display_name()  # Accessible
print(obj.name)  # Accessible


"""
Protected members
Protected members are identified with a single underscore (_). They are meant to be accessed only within the class or its subclasses.
"""

class Protected:
    def __init__(self):
        self._age = 30  # Protected attribute

class Subclass(Protected):
    def display_age(self):
        print(self._age)  # Accessible in subclass

obj = Subclass()
obj.display_age()

"""
Private members
Private members are identified with a double underscore (__) and cannot be accessed directly from outside the class. Python uses name mangling to make private members inaccessible by renaming them internally.

Note: Python’s private and protected members can be accessed outside the class through python name mangling.
"""
class Private:
    def __init__(self):
        self.__salary = 50000  # Private attribute

    def salary(self):
        return self.__salary  # Access through public method

obj = Private()
print(obj.salary())  # Works
#print(obj.__salary)  # Raises AttributeError

# Passing Values
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")

emp = Employee("Sukhi", 25, 50000)
emp.display_details()


class ProtectedData:
    def __init__(self, name, age, salary):
        self._name = name
        self._age = age
        self._salary = salary
    

class SubClassData(ProtectedData):
    def display_details(self):
        print("Protected Data")
        print(f"Name: {self._name}, Age: {self._age}, Salary: {self._salary}")



emp_show = SubClassData("Sukhi", 25, 50000)
emp_show.display_details()


class PrivateData:
    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary

    def name(self):
        return self.__name
    def age(self):
        return self.__age
    def salary(self):
        return self.__salary
    def display_details(self):
        print(f"Name: {self.name()}, Age: {self.age()}, Salary: {self.salary()}")

obj = PrivateData("Sukhi", 25, 50000)
obj.display_details()
print(obj.name())