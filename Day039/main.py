import os

os.mkdir("Day039/Data")
# if (not os.path.exists("Data")):
#   os.mkdir("Day039/Data")

for i in range(0, 5):
  os.mkdir(f"Day039/Data/Day{i+1}")