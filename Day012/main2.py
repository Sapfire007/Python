a = int(input("Enter whose table you want to be printed : "))
b = int(input("Upto which value should the product be calculated of the input number : "))
for i in range(0,b+1):
  print(a," x ",i," = ",a*i)