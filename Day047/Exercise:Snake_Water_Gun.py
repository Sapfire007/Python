import random
from pytz import timezone
from datetime import date, datetime
if (datetime.now(timezone("Asia/Kolkata")).strftime('%H:%M:%S') < "12:00:01" and datetime.now(timezone("Asia/Kolkata")).strftime('%H:%M:%S')>="00:00:00"):
  name = input("Hey there, Good morning!!! What's your name ? \n")
elif (datetime.now(timezone("Asia/Kolkata")).strftime('%H:%M:%S') < "17:00:02" and datetime.now(timezone("Asia/Kolkata")).strftime('%H:%M:%S') > "12:00:01"):
  name = input("Hey there, Good afternoon!!! What's your name ? \n")
elif (datetime.now(timezone("Asia/Kolkata")).strftime('%H:%M:%S') <= "23:59:59" and datetime.now(timezone("Asia/Kolkata")).strftime('%H') > "17:00:02"):
  name = input("Hey there, Good evening!!! What's your name ? \n")

confirmation = ""
while(confirmation.capitalize()!="Yes"):
  confirmation = input("Are you ready for the game ? : ")
  print("Processing...")

gamech = ["Snake","Water","Gun"]
playerScore = 0
CPUScore = 0
while((playerScore or CPUScore)< 5 ):
  userCh = 0
  print("Enter 1 to play Snake.")
  print("Enter 2 to play Water.")
  print("Enter 3 to play Gun.")
  while(userCh not in ("1", "2", "3")):
    userCh = input("Enter your choice : ")
    print("Processing...")

  print("CPU is choosing...")
  CPUCh = random.choice(gamech)
  print(f"CPU played {CPUCh}")
  if(userCh=="1" and CPUCh=="Snake"):
    CPUScore = CPUScore + 0
    playerScore = playerScore + 0
    print("Draw")
    print(f"Current scores :\n CPU : {CPUScore}\t\t\t {name} : {playerScore}")
  
  if (userCh=="1" and CPUCh=="Water"):
    # CPUScore = CPUScore + 0
    playerScore = playerScore + 1
    print(f"{name} scores.")
    print(f"Current scores :\n CPU : {CPUScore}\t\t\t {name} : {playerScore}")

  if(userCh=="1" and CPUCh=="Gun"):
    CPUScore = CPUScore + 1
    # playerScore = playerScore +  0
    print("CPU scores.")
    print(f"Current scores :\n CPU : {CPUScore}\t\t\t {name} : {playerScore}")

  if(userCh=="2" and CPUCh=="Snake"):
    CPUScore = CPUScore+1
    print("CPU scores.")
    print(f"Current scores :\n CPU : {CPUScore}\t\t\t {name} : {playerScore}")

  if(userCh=="2" and CPUCh=="Water"):
    CPUScore = CPUScore + 0
    playerScore = playerScore + 0
    print("Draw")
    print(f"Current scores :\n CPU : {CPUScore}\t\t\t {name} : {playerScore}")

  if(userCh=="2" and CPUCh=="Gun"):
    playerScore = playerScore + 1
    print(f"{name} scores.")
    print(f"Current scores :\n CPU : {CPUScore}\t\t\t {name} : {playerScore}")

  if(userCh=="3" and CPUCh=="Snake"):
    playerScore = playerScore + 1
    print(f"{name} scores.")
    print(f"Current scores :\n CPU : {CPUScore}\t\t\t {name} : {playerScore}")

  if(userCh=="3" and CPUCh=="Water"):
    CPUScore = CPUScore + 1
    print("CPU scores.")
    print(f"Current scores :\n CPU : {CPUScore}\t\t\t {name} : {playerScore}")

  if(userCh=="3" and CPUCh=="Gun"):
    playerScore = playerScore + 0
    CPUScore = CPUScore + 0
    print(f"{name} scores.")
    print(f"Current scores :\n CPU : {CPUScore}\t\t\t {name} : {playerScore}")

  userCh = ""
  CPUCh = ""

if (playerScore > CPUScore):
  print(f"Congratulations {name}! You won!!!")

else:
  print("CPU wins!!!")