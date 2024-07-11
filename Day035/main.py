# Enumerate Function in Python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
for index,fruit in enumerate(fruits, start=1):
  print(f"{index}. {fruit}")

colors = []
store = ""
storecount = int(input("Enter the numer of colors you want to store : "))
for i in range(storecount):
  store = input(f"{i+1}. Enter color name : ")  #String formatting was necessary here
  colors.append(store)
  store = ""

for index2,color in enumerate(colors,start=1):
  print(f"{index2}. {color}") 