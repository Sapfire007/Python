# Decorators in Python

'''
Python Decorators:

Python decorators are a powerful and versatile tool that allow you to modify the behavior of functions and methods. They are a way to extend the functionality of a function or method without modifying its source code.

A decorator is a function that takes another function as an argument and returns a new function that modifies the behavior of the original function. The new function is often referred to as a "decorated" function.

Decorators are a powerful and flexible feature in Python that can be used to add functionality to functions and methods without modifying their source code. They are a great tool for separating concerns, reducing code duplication, and making your code more readable and maintainable.

In conclusion, python decorators are a way to extend the functionality of functions and methods, by modifying its behavior without modifying the source code. They are used for a variety of purposes, such as logging, memoization, access control, and more. They are a powerful tool that can be used to make your code more readable, maintainable, and extendable.
'''

def greet(fx):
  def modifiedfx(*args, **kwargs):             #*args, **kwargs are done to take arguments for add function
    
    """
    The special syntax *args in function definitions in Python is used to pass a variable number of arguments to a function. It is used to pass a non-keyworded, variable-length argument list. 

    The syntax is to use the symbol * to take in a variable number of arguments; by convention, it is often used with the word args.
    """
    """
    The special syntax **kwargs in function definitions in Python is used to pass a keyworded, variable-length argument list. We use the name kwargs with the double star. The reason is that the double star allows us to pass through keyword arguments (and any number of them).
    """
    
    print("Hey there!")
    fx(*args, **kwargs)
    print("End of this function.")
  return modifiedfx

@greet    #or #@greet  (greet is commented) 
def hello():
  print("Hello world!")

def add(a,b):
  print(a+b)

hello()     #or #greet(hello)()
greet(add)(3,4)