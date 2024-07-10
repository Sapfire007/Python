# Exception Handling in Python
a = input("Enter a number : ")
print(f"Multiplication table of {a} is :")
try:
  for i in range(1,11):
    print(f"{a} x {i} = {int(a)*i}")

except Exception as e:
  print(e)
#Or it can be written as:
#except:
#  print("Invalid input")
print("Some important lines of code.")
try:
  num = int(input("Enter any number : "))
  a = [4,7]
  print(a[num])

except ValueError:
  print("Given input is not an integer")

except IndexError:
  print("Index error")
  
print("End of program.")

try:
  result = 100 / 2
except ZeroDivisionError:
  print(f"Division Error")
else:
  print("Result is", result)

try:
  result = 10 / 0
except ZeroDivisionError:
  print("Division by zero!")
finally:
  print("This block of code will always execute.")

try:
  raise ValueError("This is a custom error message.")
except ValueError as e:
  print("An error occurred:", str(e))