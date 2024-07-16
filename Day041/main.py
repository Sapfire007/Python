# File IO in Python
f = open('Day041/myfile.txt','r') #'r' mode is also the default mode
# f = open('Day041/myfile.txt','w') Then program wont be executed because code is written according to read or 'r' mode
print(f)
text = f.read()
print(text)
f.close()


"""
Modes in file:

There are various modes in which we can open files.

read (r): This mode opens the file for reading only and gives an error if the file does not exist. This is the default mode if no mode is passed as a parameter.

write (w): This mode opens the file for writing only and creates a new file if the file does not exist.

append (a): This mode opens the file for appending only and creates a new file if the file does not exist.

create (x): This mode creates a file and gives an error if the file already exists.

text (t): Apart from these modes we also need to specify how the file must be handled. t mode is used to handle text files. t refers to the text mode. There is no difference between r and rt or w and wt since text mode is the default. The default mode is 'r' (open for reading text, synonym of 'rt' ).

binary (b): used to handle binary files (images, pdfs, etc).
"""


g = open('Day041/myfile2.txt','w')
# g = open('Day041/myfile.txt','w') #if myfile.txt was opened instead of myfile2.txt all its pre-stored internal content would get overwritten and erased
print(g)
textinmyfile2 = g.write("This text file is made by python")
print(textinmyfile2) #The number 32 represents the number of characters written to the file "myfile2.txt".
print(type(textinmyfile2)) 
g.close()
g = open('Day041/myfile2.txt','r')
text2 = g.read()
print(text2)
g.close()

# h = open('Day041/myfile3.txt','w')
# h.write("Hello World!!!  will be appended each time in this myfile3.txt file when the main.py file within the Day041 is executed : ")
# h.close()
# Created the above mentioned myfile3.txt with python, cuz why not ;)

h = open('Day041/myfile3.txt','a')
h.write("Hello World!!! ")
h.close()
with open('Day041/myfile3.txt','a') as h:
  h.write(",(Separated by append within with statement) ")

h = open('Day041/myfile3.txt','r')
text3 = h.read()
print(text3)
h.close()