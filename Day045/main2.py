from functools import reduce

# List of numbers : 
numbers = [1,2,3,4,5]

# Calculate the sum of numbers using the reduce function :
def mysum(x,y):
  return x+y

sum = reduce(mysum,numbers)
# Print the sum :
print("Sum of the list of numbers is : ",sum,", and the type of sum variable which has been printed is : ",type(sum))