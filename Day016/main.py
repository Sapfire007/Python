def CalcAvg(a=4,b=7):          #Assigning a = 4; b = 7 by default
  print("Average of the 2 input numbers is : ",(a+b)/2)

#CalcAvg(2,3)
CalcAvg()
#CalcAvg(5)                #Here 5 is the value for a
#CalcAvg(b=25)             #Assigning the value of b without a
#CalcAvg(b=10,a=57)        #Keyword Argument
def CalcAvg2(y,x=70):        #n Python, parameters with default values must come after parameters without default values. This is because the order of parameters matters. When the function is called, the values are assigned based on their position in the function call.
  print("Average of the 2 input numbers is : ",(x+y)/2)
  
CalcAvg2(57)

def AutoCalcAvg(*numbers):
  print(type(numbers))
  sum = 0
  for i in numbers:
    sum = sum + i
  # print("Average is : ", sum/len(numbers))
  return(sum/len(numbers))

c = AutoCalcAvg(1,2,3,4,5,6,7,8,9,10)
print("Average is : ",c)

def name(**name):
    print(type(name))         #dictionay
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname="Buchanan", lname="Barnes", fname="James")