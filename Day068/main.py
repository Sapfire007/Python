# Multiple Inheritance in Python 
class Employee:
  def __init__(self,name):
    self.name = name

  def show(self):
    print(f"The name of this employee is : {self.name}")

class Sports:
  def __init__(self,sport):
    self.sport = sport

  def show(self):
    print(f"The name of this sport is : {self.sport}")

class SportspersonEmployee(Employee,Sports):    #If this line was written as class SportspersonEmployee(Sports,Employee):      #Check comment in line 24 for output
  def __init__(self, name, sport):
    self.name = name
    self.sport = sport

person1 = SportspersonEmployee("Saptarshi","Football")
print(person1.name)
print(person1.sport)
person1.show()    #It would have displayed : "The name of this sport is : Football"
print(SportspersonEmployee.mro())
"""
Method resolution order in Python Inheritance:
Method Resolution Order(MRO) it denotes the way a programming language resolves a method or attribute. Python supports classes inheriting from other classes. The class being inherited is called the Parent or Superclass, while the class that inherits is called the Child or Subclass. In python, method resolution order defines the order in which the base classes are searched when executing a method. First, the method or attribute is searched within a class and then it follows the order we specified while inheriting. This order is also called Linearization of a class and set of rules are called MRO(Method Resolution Order). While inheriting from another class, the interpreter needs a way to resolve the methods that are being called via an instance. Thus we need the method resolution order
Source: https://www.geeksforgeeks.org/method-resolution-order-in-python-inheritance/
"""