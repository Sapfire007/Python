# factorial(7) = 7*6*5*4*3*2*1
# factorial(0) = 1
# factorial = n*(n-1)!
def factorial(n):
  if(n==0  or n==1):
    return 1
  else:
    return n*factorial(n-1)

a = int(input("Enter a number whose factorial is to be calculated : "))
print("Factorial of ",a," is : ",factorial(a))


# Fibonacci series : f(n) = f(n-1)+f(n-2)
sum = 0
def fibonacci(n):
  if(n==0):
    return 0
  elif(n==1):
    return 1
  else:
    sum = fibonacci(n-1)+fibonacci(n-2)
    return sum

b = int(input("Enter the fibonacci term to be calculated : "))
print(b,"st/nd/th fibonacci term is : ",fibonacci(b))