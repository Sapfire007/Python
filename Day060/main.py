# Class Methods as Alternative Constructors in Python
class Employee:
  def __init__(self, name, salary):
    self.name = name
    self.salary = salary

  @classmethod
  def rawString(cls, inpstr):
    return cls(inpstr.split("-")[0],int(inpstr.split("-")[1]))    

emp1 = Employee("Saptarshi", 100000)
print(emp1.name)
print(emp1.salary)
data = "Sap-100000"
empA = Employee(data.split("-")[0], int(data.split("-")[1]))
print(empA.name)
print(empA.salary)
dataBulk = "Dave-85000"
emp2 = Employee.rawString(dataBulk)
print(emp2.name)
print(emp2.salary)