# Shutil Module in Python

import shutil
import os
shutil.copy("Day074/main.py","Day074/copiedMain.py")
# shutil.copy2("Day074/main.py","Day074/copiedMain.py")
shutil.copytree("Day074/containFolder","Day074/copiedContainFolder")
shutil.move("Day074/copiedContainFolder/blank.txt","Day074/")
shutil.rmtree("Day074/ToBeDeleted")
os.remove("Day074/toBeDeleted.py")