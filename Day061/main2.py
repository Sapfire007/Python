"""
The __dict__ attribute:
__dict__: The __dict__ attribute returns a dictionary representation of an object's attributes. It is a useful tool for introspection.
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.salary = 75000

p = Person("John", 30)
print(p.__dict__)



"""
The help() mehthod:
help(): The help() function is used to get help documentation for an object, including a description of its attributes and methods. Example:
"""
print(help(Person))