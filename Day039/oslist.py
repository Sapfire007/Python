import os

folders = os.listdir("Day039/Data")
print(folders)
print(type(folders))
for folder in folders:
  print(folder)

# with open("Day039/Data/Practicefolders:Day3/fakeMain.md", "w"):
#   pass
print("\n")
for folder in folders:
  print(folder)
  print(os.listdir(f"Day039/Data/{folder}"))

print(os.getcwd())
# os.chdir("/home")
# print(os.getcwd)