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