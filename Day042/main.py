f = open('Day042/myfile.txt','r')
while True:
  line = f.readline()
  if not line:
    break     #reading the line discontinues
  print(line) #The prior read line stored is now printed

f.close()
print("\n")

f = open('Day042/myfile.txt','r')
print(f.readline())
print(f.readline())
f.close()
print("\n")
f = open('Day042/myfile.txt','r')
print(f.readline(5))
f.close()
print("\n")


g = open('Day042/myfile2.txt','r')
i = 0
while True:
  i = i+1
  line1 = g.readline()
  if not line1:
    break
  m1 = line1.split(",")[0]    #This is in string
  m2 = int(line1.split(",")[1])  #This is in int
  m3 = line1.split(",")[2]
  print(f"Marks of student : {i} in Mathematics is : {m1}")
  print(f"Marks of student : {i} in English is : {m2}")
  print(f"Marks of student : {i} in Science is : {m3}")

g.close()
print("\n")


h = open('Day042/myfile3.txt','w')
lines = ['line 1\n','line 2\n','line 3\n','line 4\n',]
h.writelines(lines)
h.close()
h = open('Day042/myfile3.txt','r')
text = h.read()
print(text)
h.close()

'''
This will write the strings in the lines list to the file myfile.txt. The \n characters are used to add newline characters to the end of each string.

Keep in mind that the writelines() method does not add newline characters between the strings in the sequence. If you want to add newlines between the strings, you can use a loop to write each string separately:

f = open('myfile.txt', 'w')
lines = ['line 1', 'line 2', 'line 3']
for line in lines:
    f.write(line + '\n')
f.close()

'''