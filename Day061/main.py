# dir, __dict__ and help method in Python
'''
We must look into dir(), __dict__() and help() attribute/methods in python. They make it easy for us to understand how classes resolve various functions and executes code. In Python, there are three built-in functions that are commonly used to get information about objects: dir(), dict, and help(). Let's take a look at each of them:
'''

"""
The dir() method:
dir(): The dir() function returns a list of all the attributes and methods (including dunder methods) available for an object. It is a useful tool for discovering what you can do with an object.
"""
x = [1,2,3]
print(dir(x))
print("\n")
print(x.__add__)
print("\n")

print("\n")
y = (1,2,3)
print(dir(y))
print("\n")
print(y.__add__)