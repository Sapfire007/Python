import numpy as np
n1 = np.array([10, 20, 30, 40, 50])
print(f"n1 = {n1}\nand its type is {type(n1)}")

n2 = np.array([[10, 20, 30, 40, 50],[50, 40, 30, 20, 10]])
print(n2)
print("\n")
print("\n")


#np.zeroes(())
n3 = np.zeros((1,2))
print(n3)
print("\n")
n4 = np.zeros((3,5))
print(n4)
print("\n")
print("\n")


#np.full((),)
n5 = np.full((3,4),7)
print(n5)
print("\n")
print("\n")


#np.arange()
n6 = np.arange(10,76)
print(n6)
print("\n")
n7 = np.arange(10,76,5)
print(n7)
print("\n")
print("\n")

#np.random.randint()
n8 = np.random.randint(1,100)
print(n8)
print("\n")
n9 = np.random.randint(1,100,7)
print(n9)