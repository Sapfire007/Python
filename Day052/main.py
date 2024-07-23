class Employee:
  def __init__(self, fname, lname):
    self.fname = fname
    self.lname = lname
    # self.email = fname+"."+lname+"@email.com"

  def explain(self):
    return f"This employee is {self.fname} {self.lname}"

  @property
  #The getter in this code is implicitly defined by the @property decorator. It's used to provide a clean way to access the email value without directly accessing the fname and lname attributes.
  def email(self):
    if (self.fname == None or self.lname == None):
      return "Email not found."
    return self.fname+"."+self.lname+"@email.com"

  @email.setter
  def email(self, string):
    names = string.split("@")[0]         # names is a string which stores the first index of the split list ["this.that","email.com"]
    self.fname = names.split(".")[0]
    self.lname = names.split(".")[1]

  @email.deleter
  def email(self):
    self.fname = None
    self.lname = None

obj1 = Employee("Peter","Jones")
obj2 = Employee("Manoj","Yadav")

print(obj1.explain())
# print(obj1.email())      #If obj1.email() is called like a normal function, then the concept of data encapsulation is not preserved
print(obj1.email) #Here data is encapsulated and if there is no @property decorator then an object will be printed

obj1.fname = "Pete"
print(obj1.email)

obj1.email = "this.that@email.com"
print(obj1.email)

del obj1.email
print(obj1.email)