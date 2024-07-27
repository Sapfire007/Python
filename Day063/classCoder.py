class Coder:
  def __init__(self,name):
    self.name = name

  def __len__(self):
    i = 0
    for char in (self.name):
      i = i + 1
    return i

  def __str__(self):
    return f"The name of this employee is {self.name} (Made with __str__)"

  def __repr__(self):   #This will be executed if __str__ is not present
    return f"The name of this employee is {self.name} (Made with __repr__)"

#Follow emp.py

"""
__str__ and __repr__ methods:
The str and repr methods are both used to convert an object to a string representation. The str method is used when you want to print out an object, while the repr method is used when you want to get a string representation of an object that can be used to recreate the object.
"""