#  GeneraTORS
"""
a generator func is special function that returns an iterator objects.
Instead of using return to send back a single value, generator functions use yield to produce a series of results over time. 
This allows the function to generate values and pause its execution after each yield, maintaining its state between iterations.
"""
def mygenerator(n):
    for i in range(n):
        yield i **3

mygen = mygenerator(300)
# print(mygen)
# print(next(mygen))  # prints 0
# print(next(mygen))  # prints 1
# print(next(mygen))  # prints 2
for x in mygen:
    print(x)  # prints values


# Iterators
"""
An iterator is an object that defines the __iter__() and __next__() methods.
The __iter__() method returns the iterator object itself, and the __next__() method returns the next
value from the iterator. When there are no more values to return, the __next__() method raises
a StopIteration exception.
"""
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration
myit = MyIterator([1, 2, 3])
for x in myit:
    print(x)  # prints values
    """
    The __iter__() method is called when the iterator object is created, and it returns the iterator
    object itself. The __next__() method is called repeatedly to retrieve the next value from the
    iterator. When there are no more values to return, the __next__() method raises a Stop
    Iteration exception.
    """
    

"""
Iterator	
Class is used to implement an iterator
Local Variables aren’t used here.                                         
Iterators are used mostly to iterate or convert other objects to an iterator using iter() function.                                                               	Generators are mostly used in loops to generate an iterator by returning all the values in the loop without affecting the iteration of the loop
Iterator uses iter() and next() functions
Every iterator is not a generator

Generator

Function is used to implement a generator.
All the local variables before the yield function are stored. 
Generators are mostly used in loops to generate an iterator by returning all the values in the loop without affecting the iteration of the loop
Generator uses yield keyword
Every generator is an iterator
"""