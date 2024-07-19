# Lambda functions in Python

def double(x):
  return x*2

print(double(5))

def fncall(fx, value):
  return 6 + fx(value)    # Here 6 + cube(2) = 6 + 8 = 14

triple = lambda x: x*3
cube = lambda x: x*x*x
avg = lambda x,y: (x+y)/2    # We can use the function for multiple values 

print(triple(5))
print(cube(10))
print(avg(4,6))
print(fncall(cube,2))
print(fncall(lambda x: x*x*x,2)) # Same as line no. 18
print(fncall(lambda x: x*x,2)) # No function is made by the name of square still lambda function does the job remaining a no named / anonymous function.