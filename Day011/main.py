print("Enter the number of day of the week")
a = int(input("Enter your choice : "))
match a:
  case 1:
    print("It's Monday")
  case 2:
    print("It's Tuesday")
  case 3:
    print("It's Wednesday")
  case 4:
    print("It's Thursday")
  case 5:
    print("It's Friday")
  case 6:
    print("It's Saturday")
  case 7:
    print("It's Sunday")
  case _ if (a>7 and a<10):
    print("Wrong input, you have input a value within 10 but exceeds 7")
  case _ if a<=0:
    print("Wrong input, you have input a negative value")
  case _:           # (_) is used for default cases in python
    print("Wrong input")