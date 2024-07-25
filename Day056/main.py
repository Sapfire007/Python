# Static Methods in Python
"""
Static methods in Python are methods that belong to a class rather than an instance of the class. They are defined using the @staticmethod decorator and do not have access to the instance of the class (i.e. self). They are called on the class itself, not on an instance of the class. Static methods are often used to create utility functions that don't need access to instance data.
"""
class Math:
  def __init__(self, num):
    self.num = num

  def addtonum(self, n):
    self.num = self.num + n

  @staticmethod
  def add(a, b):
    return a+b

def add(x,y):
  return x + y

a = Math(7)
print(a.num)
a.addtonum(3)
print(a.num)
print(Math.add(10, 4))
print(a.add(10,5))
print(add(4,3))   #Method used here is out of class: Math