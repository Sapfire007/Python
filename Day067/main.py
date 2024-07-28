# Single Inheritance in Python
class Animal:
  def __init__(self, name, species):
      self.name = name
      self.species = species

  def make_sound(self):
      print("Sound made by the animal")

class Dog(Animal):
  def __init__(self, name, breed):
    Animal.__init__(self, name, species="Dog")
    self.breed = breed

  def make_sound(self):
    print("Bark!")

d = Dog("Goldie","Golden Retriever")
d.make_sound()

ani1 = Animal("Flying Squirrel","Squirrel")
ani1.make_sound()


# Quick Quiz: Implement a Cat class by using the animal class. Add some methods specific to cat
class Cat(Animal):
  def __init__(self, name, breed):
    super().__init__(name, species="Cat")
    self.breed = breed

  def make_sound(self):
    print("Meow!")

c = Cat("Tom","Tuxedo")
c.make_sound()


#Others
print(Animal.__dict__)
print(c.__dict__)