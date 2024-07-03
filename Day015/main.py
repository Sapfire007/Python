#Functions in Python
def CalcGmean(a,b):            #These are user defined functions
  Gmean = (a*b)**(1/2)
  print("The geometric mean of your entered 2 numbers is : ",Gmean)

def CalcMax(a,b):     #def function_name(parameters):
  if(a>b):
    print("The greatest input number is : ",a)
  elif(b>a):
    print("The greatest input number is : ",b)
  else:
    print("Both input values are the same")

def CalcMin(a,b):
  pass  #This allows python to go ahead instead for searching and executing the function body
x = int(input("Enter the first number : ")) 
y = int(input("Enter the second number : "))
CalcGmean(x,y)     #Calling the function
CalcMax(x,y)