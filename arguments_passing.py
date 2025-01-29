# Arguments Passing
# :args: arguments passed to the function
# :return: return value of the function
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

def my_function1(*args):
    print("hello", args)
    # Function Body
    for arg in args:
       print(arg)

my_function1(1, True, "Hello", "world")


def my_function2(**kwargs):
   print(kwargs)
   # Function Body
   for key, value in kwargs.items():
      print(f"{key} = {value}")

my_function2(name="John", age=30, city="New York")

def my_function3(*args, **kwargs):
   
   print("hello", args)
   print(kwargs)
   # Function Body
   for arg in args:
    print(arg)

    
    for key, value in kwargs.items():
      print(f"{key} = {value}")

      
my_function3(1, True, "Hello", "world", name="John", age=25, address="Janakpur")