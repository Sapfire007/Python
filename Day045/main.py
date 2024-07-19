# Map and Filter in Python

# Map
def cube(x):
  return x*x*x

l1 = [0,1,2,3,4,5,6,7,8,9]
nl1 = []
for items in l1:
  nl1.append(cube(items))

print(nl1)
print("\n")


newl = map(lambda x: x*x,l1)   # newl = map(cube,l1) # this could also be done
print("This is the map object used here : ",newl)
print("This is the type of map object used here : ",type(newl))
print("Map object as list (List items are squared): ",list(newl))
print("\n")


# Filter
def filter_func(a):
  return a>4
newl2 = filter(filter_func,l1)
print("This is the filter object used here : ",newl2)
print("This is the type of filter object used here : ",type(newl2))
print("Filter object as list (List items are squared): ",list(newl2))
print("\n")