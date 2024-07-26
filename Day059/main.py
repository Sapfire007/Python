# Class Methods in Python
class Employee:
  company = "CPY A"
  def show(self):
    print(f"The name of employee is : {self.name} and is working in {self.company}.")

  def changeCompany(hey, newCompany):      #self,hey,etc anything can be written its just the object.
    hey.company = newCompany

  #Now using the class method decorator
  @classmethod
  def changeCompanyOfClass(cls, transferCompany):
    cls.company = transferCompany

emp1 = Employee()
emp1.name = "Saptarshi"
emp1.show()
emp1.changeCompany("CPY B")
emp1.show()
print(emp1.company)    #TO BE NOTED : Output = CPY B
print(Employee.company)    #TO BE NOTED : Output = CPY A
emp1.changeCompanyOfClass("CPY X")
emp1.show()      #Still self.company is CPY B   #THis is because class methods affect the class-level attributes, but individual instances retain their own attribute values. That’s why the 24th line’s output still shows “CPY B” for emp1.company
print(emp1.company)    #TO BE NOTED : Output = CPY B   #THis output would have been CPY X if emp1's company had not been modified through changeCompany instance method in line 18
print(Employee.company)    #TO BE NOTED : Output = CPY X