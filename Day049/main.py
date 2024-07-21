# Classes and Objects in Python
class Details:
  name = "Saptarshi"
  age = 17
  occupation = "Student"

  def info(self):
    print(f"{self.name} is a {self.occupation}")   # self means that object for which the method is being called.
    
    # self parameter is an reference to the current instance of the class and is used to access variables that belong to the class
    
    """
    self parameter:
    
    The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

    It must be provided as the extra parameter inside the method definition.
    """


obj1 = Details()
print(obj1.name, obj1.occupation, obj1.age)
obj1.info()
print("\n")

obj2 = Details()
obj2.name = "David"
obj2.occupation = "Freelancer"
print(obj2.name, obj2.occupation, obj2.age)
obj2.info()