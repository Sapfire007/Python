import numpy as np

X = np.array ( [ [ 8, 10 ], [ -5, 9 ] ] )
Y = np.array ( [ [ 2, 6 ], [ 7, 9 ] ] )

print ("Addition of Two Matrix : \n ", X+Y)

print ("Subtraction of Two Matrix : \n ", X-Y)

print ("Multiplication of Two Matrix : \n ", X*Y)

print ("Division of Two Matrix : \n ", X/Y)

print ("dot product of Two Matrix : \n ", X@Y)

print ( " Transpose Matrix is : \n ", np.transpose(X))

print(" Inverse Matrix is : \n ",np.linalg.inv(X))