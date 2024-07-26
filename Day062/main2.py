class Employee:
  def __init__(self,name,id):
    self.name = name
    self.id = id
    self.country = "India"

class Coder(Employee):
  def __init__(self,name,id,lang):
    super().__init__(name,id)
    self.lang = lang

emp1 = Employee("Sam",578)
print(emp1.__dict__)
emp2 = Coder("Saptarshi",47,"Python")
print(emp2.__dict__)
print(emp2.country)