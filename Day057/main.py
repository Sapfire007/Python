# Instance variables vs Class variables in Python
class Employee:
  companyName = "SapTech"     #This is a class variable
  noOfEmployee = 0    #One good example of use case scenario of class variable.
  def __init__(self, name):
    self.name = name        #These are instance variables
    self.project = "Alpha05"   #These are instance variables
    Employee.noOfEmployee += 1

  def showDetails(self):
    print(f"The name of the employee is : {self.name} and are working on the current project of : {self.project} in {self.companyName}\nCurrent size of the company : {self.noOfEmployee}")


emp1 = Employee("Saptarshi")
emp1.project = "Charlie45"
emp1.companyName = "SapTech-India"
emp1.showDetails()
Employee.companyName = "SapTech Global Industries"
print(Employee.companyName)
# Employee.showDetails(emp1) #Same as : emp1.showDeatails()
emp2 = Employee("Aryan")
emp2.companyName = "SapTech-Singapore"
emp2.showDetails()
emp3 = Employee("Rohan")
emp3.showDetails()