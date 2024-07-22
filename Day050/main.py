class Person:
  # name = "Saptarshi"
  # occupation = "Student"
  def __init__(self, n, o):     #Syntax of Python Constructor
    print("Hello World!")
    #This method will be invoked everytime an object is created
    self.name = n
    self.occupation = o

  def info(self):
    print(f"{self.name} is a {self.occupation}")


obj1 = Person("Saptarshi","Student")    # obj1 is also an argument in place of 'self'
obj1.info()

obj2 = Person("Shreyas","Singer")
obj2.info()

obj2 = Person(1,2)        #Integers can also be passed in arguments
obj2.info()

# obj1.name = "Shreyas"
# obj1.occupation = "Singer"
# obj1.info()