# Type Hinting
"""
Python is a dynamically typed language, which means you never have to explicitly indicate what kind of variable it is. 
But in some cases, dynamic typing can lead to some bugs that are very difficult to debug, and in those cases, Type Hints or Static Typing can be convenient.
"""

# def factorial(i):
#     if i<0:
#         return None
#     if i == 0:
#         return 1
#     return i * factorial(i-1)

# # passing an integer to the function
# print(factorial(4))

# passing a string to the function
# print(factorial("4")) #shows error here Tpe error TypeError: '<' not supported between instances of 'str' and 'int'

# passing a floating point number to the function
# print(factorial(5.01)) # sho3ws error TypeError: unsupported operand type(s) for *: 'float' and 'NoneType'

def multiply(x:int, y:int):
    return x * y
print(multiply(5, 6))
print(multiply(5, "hello"))


def my_function(myparameter:int) -> str:
    return "Hello, " + myparameter
# print(my_function(5)) # shows error TypeError: can only concatenate str (not "int")


def my_function1(myparameter:int) -> str:
    return myparameter
print(my_function1(5))

def my_funtion2(other:int) -> int:
    return other
print(my_funtion2("hello")) # shows error TypeError: unsupported operand type(s)
# for +: 'str' and 'int'  # this is because the function is expecting 
# an integer but we are passing a string
# we can use type checking to check the type of the variable before passing it to the function


def list_object(parameter:list[int]):
    return parameter
print(list_object([1, 2, 3, 4, 5])) # prints
# [1, 2, 3, 4, 5]
print(list_object([1, 2, 3, "hello", 5])) # shows
# error TypeError: list indices must be integers or slices, not str

print(list_object((1,2,3)))