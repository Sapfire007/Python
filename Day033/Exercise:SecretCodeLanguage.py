"""
Exercise 4: Secret Code Language

Instructions :

Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

Coding:
if the word contains atleast 3 characters, remove the first letter and append it at the end
  now append three random characters at the starting and the end
else:
  simply reverse the string

Decoding:
if the word contains less than 3 characters, reverse it
else:
  remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

Your program should ask whether you want to code or decode

"""

def storeinlist(b):
  c = b.strip()+" "
  l1 = []
  # print(c)
  store = ""
  for i in range(len(c)):
    # print(i)
    if (i<=len(c) and c[i]!=" "):
      store = store+c[i]

    else:
      l1.append(store)
      store = ""
      
  # print(l1)
  l1 = [word for word in l1 if word] # Keep only non-empty strings
  # print(l1)
  return l1

def reverse(str):
  blankstr = ""
  for i in str:
    blankstr = i+blankstr

  return blankstr


a=input("Enter 1 to use : Encryptor \nEnter 2 to use : Decryptor \nEnter your choice : ")
if (a.isnumeric()) is False:
  raise ValueError("Non integers are not accepted. ~Sap")

else:
  a = int(a)
  match a:
    case 1:
      print("Encryptor loaded...")
      b = input("Enter your message : ")
      reqlist = storeinlist(b)
      # print(reqlist)
      outputlist = []
      for i in reqlist:
        # print(i)
        if(len(i)>=3):
          zeroIndstore = i[0]
          nw = i[1:]
          # print(nw)
          newi="Sap"+nw+(zeroIndstore)+"Sec"
          zeroIndstore = ""
          # print(newi)
          outputlist.append(newi)

        else:
          newi = reverse(i)
          outputlist.append(newi)
      # print(outputlist)
      finalstr = ""
      for i in outputlist:
        finalstr = finalstr + (i+" ")

      print(f"Your encrypted message is : {finalstr}")
          
    case 2:
      print("Decryptor loaded...")
      b = input("Enter your message : ")
      reqlist = storeinlist(b)
      # print(reqlist)
      outputlist = []
      for i in reqlist:
        if(len(i)>=3):
          newitemp = i[3:-3]
          lastindstore = newitemp[-1]
          newitemp2 = newitemp[:-1]
          newitemp2 = lastindstore+newitemp2
          outputlist.append(newitemp2)

        else:
          newitemp2 = reverse(i)
          outputlist.append(newitemp2)

      # print(outputlist)
      finalstr = ""
      for i in outputlist:
        finalstr = finalstr + (i+" ")

      print(f"Your encrypted message is : {finalstr}")
  
    case _:
      print("Invalid input.")