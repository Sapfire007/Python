# Method Overriding in Python
class Shape:
  def __init__(self,x,y):
    self.x = x
    self.y = y

  def area(self):
    return self.x * self.y

class Circle(Shape):
  def __init__(self, radius):
      self.radius = radius
      super().__init__(radius,radius)

  def area(self):
      return 3.14 * super().area()

rec = Shape(7,4)
print(f"The area for the rectangle is : {rec.area()} sq units")
c = Circle(5)
print(f"The area for the circle is : {c.area()} sq units")