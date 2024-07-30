# Generators in Python
def my_generator():
  for i in range(20):
    yield i

gen = my_generator()
print(next(gen))
print(next(gen))

for i in "Saptarshi":
  print(i)

print(next(gen))
print("\n")
for j in gen:
  print(j)

"""
Generators in Python are a powerful tool for working with large or complex data sets, allowing you to generate the values on-the-fly and store only what you need in memory. Whether you are working with a large dataset, performing complex calculations, or generating a sequence of values, generators are a must-have tool in your programming toolkit.
"""