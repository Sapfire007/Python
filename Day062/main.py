# super keyword in Python
"""
Super keyword in Python :
The super() keyword in Python is used to refer to the parent class. It is especially useful when a class inherits from multiple parent classes and you want to call a method from one of the parent classes.

When a class inherits from a parent class, it can override or extend the methods defined in the parent class. However, sometimes you might want to use the parent class method in the child class. This is where the super() keyword comes in handy.
"""
class parentClass:
  def parent_method(self):
    print("This is within parent class.")

class childClass(parentClass):
  def trial_method(self):
    print("Saptarshi")
    super().parent_method()
    print("\n")

  def child_method(self):
    print("This is within child method.")
    super().parent_method()

obj1 = childClass()
obj1.child_method()
obj1.trial_method()
obj1.parent_method()