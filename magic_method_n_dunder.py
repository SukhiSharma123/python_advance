# # Dunder
# '''
# Dunder means under score under score (__) like __init__
# '''

# class Person: # this is class 
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.__secret = 'This is a secret'

# p = Person("Sukhi Sharma", 25) # this is object of class 
# print(p.name)
# print(p.age)
# #print(p.__secret) # this will give error because it is private variable


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__private = 'This is private'

    def __add__(self, others):
        return Vector(self.x + others.x, self.y + others.y)
    
    def __repr__(self):
        return f"X: {self.x} and Y: {self.y}"
    
    def __call__(self, *args, **kwds):
        return f"Hi, this is call function and i was called!!"
    

v1 = Vector(20,30)
print(v1.x)
print(v1.y)
# print(v1.__private) # this will give error because it is private variable
v2 =Vector(30,40)
print(v2.x)
print(v2.y)
# print(v2.__private) # this will give error because it is private variable
v3 = v1 + v2 # it works on add function to add v1 and v2
print(v3.x) # it gives sum of 20 and 30 i.e v1.x and v2.x
print(v3.y) # it gives sum of 30 and 40 i.e v1.y and v2.y

print(v3) #it returns object type but if we represent it with function then it will retrurn x valiue and y value

print(v3()) # this is call function and function call  was made
print(v3.__repr__()) # this is also call function and function call was made but for representation




