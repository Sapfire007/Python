# 'is' vs '==' in Python
a = 4
b = "4"
print(a is b)   # exact location of object in memory
print(a == b) # value
print("\n")
c = [4,7,75]
d = [4,7,75]
print(c is d)           #False
print(c == d)           #True
print("\n")
e = 7
f = 7
print(e is f)        #True because integers are immutables and only 1 memory location is allocated for constants whose value is equal to 7
print(e == f)     #True because of same value
# Same goes for string
g = "Saptarshi"
h = "Saptarshi"
print(g is h)
print(g == h)
# Same goes for tuples (Tuples are immutable)
i = (4,7,75)
j = (4,7,75)
print(i is j)
print(i == j)
# Same goes for None
k = None
l = None
print(k is l)
print(k == l)
print(k is None)
print(k == None)