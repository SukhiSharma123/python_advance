"""
Documentation: https://www.geeksforgeeks.org/singleton-method-python-design-patterns/
"""

"""
What is Singleton Method in Python
Singleton Method is a type of Creational Design pattern and is one of the simplest design patterns available to us. 
It is a way to provide one and only one object of a particular type. It involves only one class to create methods and specify the objects. 
Singleton Design Pattern can be understood by a very simple example of Database connectivity. 
When each object creates a unique Database Connection to the Database, it will highly affect the cost and expenses of the project. 
So, it is always better to make a single connection rather than making extra irrelevant connections which can be easily done by Singleton Design Pattern.


Definition: The singleton pattern is a design pattern that restricts the instantiation of a class to one object.


Now let’s have a look at the different implementations of the Singleton Design pattern. 

Method 1: Monostate/Borg Singleton Design pattern
Singleton behavior can be implemented by Borg’s pattern but instead of having only one instance of the class, there are multiple instances that share the same state. 
Here we don’t focus on the sharing of the instance identity instead we focus on the sharing state. 


Double Checked Locking Singleton Design pattern
It is easy to notice that once an object is created, the synchronization of the threading is no longer useful because now the object will never be equal to None and any sequence of operations will lead to consistent results. 
So, when the object will be equal to None, then only we will acquire the Lock on the getInstance method.

"""


"""
Advantages of using the Singleton Method: 
Initializations: An object created by the Singleton method is initialized only when it is requested for the first time.
Access to the object: We got global access to the instance of the object.
Count of instances: In singleton, method classes can’t have more than one instance
Disadvantages of using the Singleton Method: 
Multithread Environment: It’s not easy to use the singleton method in a multithread environment, because we have to take care that the multithread wouldn’t create a singleton object several times.
Single responsibility principle: As the Singleton method is solving two problems at a single time, it doesn’t follow the single responsibility principle.
Unit testing process: As they introduce the global state to the application, it makes the unit testing very hard.
Applicability
Controlling over global variables: In the projects where we specifically need strong control over the global variables, it is highly recommended to use Singleton Method
Daily Developers use: Singleton patterns are generally used in providing the logging, caching, thread pools, and configuration settings and are often used in conjunction with Factory design patterns.
"""


from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):
    @abstractstaticmethod
    def get_data():
        """Implement in child class """


class PersonSingleton(IPerson):
    """ Singleton class """
    __instance = None  #private

    @staticmethod
    def get_instance():
        """ Static access method. """
        if PersonSingleton.__instance is None:
            print("No instance found")
            # PersonSingleton.__instance = PersonSingleton("Name", 20) # for p3 it gives error so we can do 
            PersonSingleton("hello", 3)
            return PersonSingleton.__instance

    def __init__(self, name, age):
        """ Virtually private constructor. """
        if PersonSingleton.__instance is not None: 
            raise Exception("This class is a singleton!")
        self.name = name
        self.age = age
        # super().__init__()#call the parent class constructor
        PersonSingleton.__instance = self

    @staticmethod
    def get_data():
        """Implement in child class """
        print(f"Name: {PersonSingleton.__instance.name} and age: {PersonSingleton.__instance.age}")
        # return PersonSingleton.get_instance().name, PersonSingleton.get_instance().age


p = PersonSingleton("Mike", 20)
print(p.get_data())  # Mike 20

# p2 = PersonSingleton("only once", 2)
# print(p2.get_data())  # Mike 20   #show error/exception because we can use it only once


p3 = PersonSingleton.get_instance()
print(p3.get_data())  # Mike 20