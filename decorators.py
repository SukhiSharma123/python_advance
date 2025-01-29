# Decorators
"""
decorators are functions which extend or modify a function without chnaging its actual function/behaviour.
it returns a new function with modified version
decorators can be called as @ and decorators name 
"""
# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func() #function is called
#         print("Something is happening after the function is called.")
    
#     return wrapper

# @my_decorator # decoratot being called
# def say_hello():
#     print("Hello!")

# say_hello()

#say_hello("Sukhi") #if we pass any arguments in the function for the decotaotrs it will show errors
# decorators can be used to add some functionality to the function without changing the function itself

# to fix error given by say_hello("Sukhi") we modify decoraots
# def my_decorator(func):
#     def wrapper(*args, **kwargs): # *args and **kwargs are used to pass any value
#         """
#         *args is used to pass any number of arguments but non-kwyword arguments
#         **kwargs is used to pass any number of keyword arguments 
#         """
#         print("Something is happening before the function is called.")
#         func(*args, **kwargs) #function is called
#         print("Something is happening after the function is called.")
#     return wrapper


# @my_decorator # decoratot being called
# def say_hello(name):
#     print(f"Hello! {name}")
# say_hello("Sukhi")


# Practical Exampels 1

# Timed

import time
def my_decorator(func):
    def wrapper(self, *args, **kwagrs):
        start_time = time.time()
        fun = func(self, *args, **kwagrs)
        end_time = time.time()
        print(f"Time taken by the function is {end_time - start_time} seconds")
        return fun
    return wrapper

# @my_decorator
# def say_hello():
#     time.sleep(2)
#     print("Hello!")
# say_hello()

@my_decorator
def cal_time(x):
    value = 1
    for i in range(1,x):
        value = value * i
    return value

cal_time(90000)

        