import this #PEP 8 #The Zen of Python #This is an easter egg in python
print("\n")
#Docstrings in python
def square(num):
  # print(num)     #If this statement existed the below wouldnt have been a docstring because doctring just comes below the function name (Comments dont interfere this condition)
  '''
  Takes a number num, returns the square of num
  '''
  print(num**2)
square(8)
print(square.__doc__)
print(type(square.__doc__))