# Magic/Dunder Methods in Python 
"""
Magic/Dunder Methods in Python:
These are special methods that you can define in your classes, and when invoked, they give you a powerful way to manipulate objects and their behaviour.

Magic methods, also known as “dunders” from the double underscores surrounding their names, are powerful tools that allow you to customize the behaviour of your classes. They are used to implement special methods such as the addition, subtraction and comparison operators, as well as some more advanced techniques like descriptors and properties.

Let’s take a look at some of the most commonly used magic methods in Python.
"""


class Employee:
  name = "Saptarshi"

  def __len__(self):
    i = 0
    for char in (self.name):
      i = i + 1
    return i

emp1 = Employee()
print(emp1.name)
print(len(emp1))

"""
__len__ method:
The len method is used to get the length of an object. This is useful when you want to be able to find the size of a data structure, such as a list or dictionary.
"""



"""
__init__ method :
The init method is a special method that is automatically invoked when you create a new instance of a class. This method is responsible for setting up the object’s initial state, and it is where you would typically define any instance variables that you need. Also called "constructor", we have discussed this method already.
"""