"""
In this example, we have a ParentClass with a parent_method and a ChildClass that inherits from ParentClass and overrides the child_method. When the child_method is called, it first prints "This is the child method." and then calls the parent_method using the super() keyword.

The super() keyword is also useful when a class inherits from multiple parent classes. In this case, you can specify the parent class from which you want to call the method.
"""
class ParentClass1:
  def parent_method(self):
      print("This is the parent method of ParentClass1.")

class ParentClass2:
  def parent_method(self):
      print("This is the parent method of ParentClass2.")

class ChildClass(ParentClass1, ParentClass2):
  def child_method(self):
      print("This is the child method.")
      # super().parent_method() #ParentClass1
      ParentClass2.parent_method(self)  # Calls the method of ParentClass2

child_object = ChildClass()
child_object.child_method()