# Access Modifiers in Python

"""
Public Access Specifier in Python :

All the variables and methods (member functions) in python are by default public. Any instance variable in a class followed by the ‘self’ keyword ie. self.var_name are public accessed.
"""

class Employee:
  def __init__(self):
    self.name = "Saptarshi"

obj1 = Employee()
print(obj1.name)


"""
Private Access Modifier:

By definition, Private members of a class (variables or methods) are those members which are only accessible inside the class. We cannot use private members outside of class.

In Python, there is no strict concept of "private" access modifiers like in some other programming languages. However, a convention has been established to indicate that a variable or method should be considered private by prefixing its name with a double underscore (__). This is known as a "weak internal use indicator" and it is a convention only, not a strict rule. Code outside the class can still access these "private" variables and methods, but it is generally understood that they should not be accessed or modified.
"""

class Employee2:
  def __init__(self):
    self.__name = "Saptarshi2"

obj2 = Employee2()
# print(obj1.__name) # Throws an AttributeError
print(obj2.__dir__())
print(obj2._Employee2__name) #Output : Saptarshi2 # Can be accessed indirectly

"""
Name mangling:
Name mangling in Python is a technique used to protect class-private and superclass-private attributes from being accidentally overwritten by subclasses. Names of class-private and superclass-private attributes are transformed by the addition of a single leading underscore and a double leading underscore respectively.

class MyClass:
  def __init__(self):
      self._nonmangled_attribute = "I am a nonmangled attribute"
      self.__mangled_attribute = "I am a mangled attribute"

my_object = MyClass()

print(my_object._nonmangled_attribute) # Output: I am a nonmangled attribute
print(my_object.__mangled_attribute) # Throws an AttributeError
print(my_object._MyClass__mangled_attribute) # Output: I am a mangled attribute

In the example above, the attribute _nonmangled_attribute is marked as nonmangled by convention, but can still be accessed from outside the class. The attribute __mangled_attribute is private and its name is "mangled" to _MyClass__mangled_attribute, so it can't be accessed directly from outside the class, but you can access it by calling _MyClass__mangled_attribute
"""


"""
Protected Access Modifier:

In object-oriented programming (OOP), the term "protected" is used to describe a member (i.e., a method or attribute) of a class that is intended to be accessed only by the class itself and its subclasses. In Python, the convention for indicating that a member is protected is to prefix its name with a single underscore (_). For example, if a class has a method called _my_method, it is indicating that the method should only be accessed by the class itself and its subclasses.

It's important to note that the single underscore is just a naming convention, and does not actually provide any protection or restrict access to the member. The syntax we follow to make any variable protected is to write variable name followed by a single underscore (_) ie. _varName.
"""

class Student:
  def __init__(self):
      self._name = "Saptarshi"

  def _funName(self):      # protected method
      return "Sapfire955"

class Subject(Student):       #inherited class
  pass

obj3 = Student()
obj4 = Subject()

# calling by object of Student class
print(dir(obj3))
print(obj3._name)      
print(obj3._funName()) 

# calling by object of Subject class
print(dir(obj4))
print(obj4._name)    
print(obj4._funName())