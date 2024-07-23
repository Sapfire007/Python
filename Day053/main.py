# Inheritance in Python
class Employee:           # Parent class
  def __init__(self, name, id):
    self.name = name
    self.id = id

  def showDetails(self):
    print(f"The name of Employee : {self.id} is {self.name}")

class Programmer(Employee):       # Programmer = Employee + (own class' function)    # Child class
  def showLanguage(self):
    print("The default language used is python.")


obj1 = Employee("Saptarshi", 7)
obj1.showDetails()

obj2 = Programmer("Ryan", 4)
obj2.showDetails()
obj2.showLanguage()