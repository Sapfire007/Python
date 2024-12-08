import numpy as np

X = np.array ( [ [ 8, 10 ], [ -5, 9 ] ] )

Y = np.array ( [ [ 2, 6 ], [ 7, 9 ] ] )

# Create a result matrix with the same dimensions

A = [[0, 0],[0, 0]]

S = [[0, 0],[0, 0]]

M = [[0, 0],[0, 0]]

D = [[0, 0],[0, 0]]

for i in range(len(X)):
  for j in range(len(Y)):
    A[i][j] = X[i][j] + Y[i][j]
    S[i][j] = X[i][j] - Y[i][j]
    M[i][j] = X[i][j] * Y[i][j]
    D[i][j] = X[i][j] / Y[i][j]

print ("Addition of Two Matrix : \n ", A)

print ("Subtraction of Two Matrix : \n ", S)

print ("Multiplication of Two Matrix : \n ", M)

print ("Division of Two Matrix : \n ", D)