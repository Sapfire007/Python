import os

for i in range(0,5):
  os.rename(f"Day039/Data/Day{i+1}",f"Day039/Data/Practicefolders:Day{i+1}")

# os.makedirs("Day039", exist_ok=True)

# # Create an empty file named "oslist.py" within "Day039"
# with open("Day039/oslist.py", "w") as f:
#   pass