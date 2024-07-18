# seek(), tell() and other functions
a = open('Day043/textfile.txt','w')
a.write("abcdefghijklmnopqrstuvwxyz\n")
a.close()

with open('Day043/textfile.txt','r') as f:
  print(type(f))

  f.seek(10)     # Move to the 10th byte in the file
  print(f.tell())    #Tells the current position
  text = f.read(5)      # Read the next 5 bytes
  print(text)

'''
seek() and tell() functions:

In Python, the seek() and tell() functions are used to work with file objects and their positions within a file. These functions are part of the built-in io module, which provides a consistent interface for reading and writing to various file-like objects, such as files, pipes, and in-memory buffers.
'''

with open('Day043/textfile2.txt','w') as g:
  g.write("Hello World!")
  g.truncate(5)
with open('Day043/textfile2.txt','r') as g:
  text2 = g.read()
  print(text2)