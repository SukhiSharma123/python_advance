# Factory  Design Pattern
"""
Factory Method is a Creational Design Pattern that allows an interface or a class to create an object, but lets subclasses decide which class or object to instantiate. 
Using the Factory method, we have the best ways to create an object. 
Here, objects are created without exposing the logic to the client, and for creating the new type of object, the client uses the same common interface.
"""


"""
Factory Method Pattern in Python
The Factory Method Pattern is a creational design pattern that provides an interface for creating objects but allows subclasses to alter the type of objects that will be created. 
It helps encapsulate object creation logic, making code more flexible and scalable.
"""

"""
abc stands for abstact class 
"""
from abc import ABCMeta, abstractmethod, abstractstaticmethod


from abc import ABC, abstractmethod

# Step 1: Create an abstract base class
class Vehicle(ABC):
    @abstractmethod
    def create(self):
        pass

# Step 2: Concrete classes implementing the interface
class Car(Vehicle):
    def create(self):
        return "Car created"

class Bike(Vehicle):
    def create(self):
        return "Bike created"

# Step 3: Factory method to create objects
class VehicleFactory:
    @staticmethod
    def get_vehicle(vehicle_type: str) -> Vehicle:
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "bike":
            return Bike()
        else:
            raise ValueError("Invalid vehicle type")

# Step 4: Client code
vehicle1 = VehicleFactory.get_vehicle("car")
print(vehicle1.create())  # Output: Car created

vehicle2 = VehicleFactory.get_vehicle("bike")
print(vehicle2.create())  # Output: Bike created



class IPerson(metaclass=ABCMeta):
    @abstractstaticmethod
    def person_method():
        """ Interface Method """
        # pass

# p1 = IPerson()
# p1.person_method()  # Raises AttributeError: 'IPerson' object has no attribute 'person

class Student(IPerson):
    def __init__(self):
        self.name = "Basic Student Class"

    def person_method(self):
        print("I am a student")


class Teacher(IPerson):
    def __init__(self):
        self.name = "Basic Teacher Class"

    def person_method(self):
        print("I am a teacher")


p1 = Student()
p1.person_method()  # Output: I am a student

p2 = Teacher()
p2.person_method()


class PersonFactory:
    @staticmethod
    def build_person(person_type):
        if person_type == "student":
            return Student()
        elif person_type == "teacher":
            return Teacher()
        else:
            raise ValueError("Invalid person type")

p3 = PersonFactory()
p3.build_person("student")  # Output: I am a student
p3.build_person("teacher")  # Output: I am a teacher
# p3.build_person("invalid")  # Raises ValueError: Invalid person type
print(p3.build_person("student"))
p4 = p3.build_person("student")
print(p4.person_method())  # Output: I am a student
print(p3.build_person("teacher").person_method())  # Output: I am a teacher
