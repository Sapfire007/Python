"""
Objective : 
Write a program to clear the clutter inside a folder on your computer. You should use os module to rename all the png images from 1.png all the way till n.png where n is the number of png files in that folder. Do the same for other file formats. For example:

sfdsf.png --> 1.png
vfsf.png --> 2.png
this.png --> 3.png
design.png --> 4.png
name.png --> 5.png
"""

import os   #importing os for the necessary functions
import shutil  #importing shutil for moving files
# print(dir(os))

if (not os.path.exists("clutteredFolder")):      #Making our required cluttered folder after check if it already exists or not
  os.mkdir("Day058/clutteredFolder")    #Making our required folder

pngFiles = os.listdir("Day058/Files")    #Listing the directory of Files in pngFiles
for file in pngFiles:           #running for loop for going through the files
  if file.endswith(".png"):        #checking for .png files
    shutil.move(f"Day058/Files/{file}","Day058/clutteredFolder")    #moves .png files to our required clutteredFolder

reqFiles = os.listdir("Day058/clutteredFolder")   #Listing the directory of .png Files in reqFiles
i = 1    #rename counter variable
for file in reqFiles:    #running for loop for going through the .png files
  if file.endswith(".png"): #this can be skipped cuz already all the files are .png
    os.rename(f"Day058/clutteredFolder/{file}",f"Day058/clutteredFolder/{i}.png") #renaming the .png files
    i += 1      #increment by 1 for rename counter variable
#End of program