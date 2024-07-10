# Finally keyword in Python
def func1():
  try:
    l1 = [1,4,7,5]
    i1 = int(input("Enter the list index : "))
    print(l1[i1])
    return 1

  except IndexError:
    print("Invalid index")
    return 0

  except ValueError:
    print("Input is not an index number")
    return 0

  finally:
    print("I will be executed always (within finally keyword) this is within function and this is its end")

  print("This will be executed (within print statement)")

x = func1()
print(f"{x} : This is the print statement's execution out of the function block")
print("\n")

try:
  l = [1,5,6,7]
  i = int(input("Enter the list index : "))
  print(l[i])

except IndexError:
  print("Invalid index")

except ValueError:
  print("Input is not an index number")

finally:
  print("I will be executed always (within finally keyword)")

print("This will be executed (within print statement)")