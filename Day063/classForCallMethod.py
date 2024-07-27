import random
import string


class Employee:
    def __init__(self, name) -> None:
        self.name = name

    def __call__(self, *args, **kwargs): # this makes the instance callable
        self.id = "".join(
            random.choices(self.name + string.ascii_letters + string.digits, k=6)
        )
        print(f"The Employee's ID: {self.id}")


e = Employee("Arpan")
e()

# Alternate program : 
"""
class shop:
    def __init__(self,sales,expenditure):
        self.sales=sales
        self.expenditure=expenditure
    def __call__(self):
        print(F"The total profit is {self.sales-self.expenditure}")
shop1=shop(15000,12000)
shop1()

Output: 
The total profit is 3000
"""


"""
__call__ method:
The call method is used to make an object callable, meaning that you can pass it as a parameter to a function and it will be executed when the function is called. This is an incredibly powerful tool that allows you to create objects that behave like functions.

These are just a few of the many magic methods available in Python. They are incredibly powerful tools that allow you to customize the behaviour of your objects, and can make your code much cleaner and easier to understand.
"""