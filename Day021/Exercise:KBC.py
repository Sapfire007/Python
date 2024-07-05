name = input("Input your name : ")
confirmation = ""
prizemoney = 5000
newPrizeMoney = prizemoney
presentPrizeMoney = 0
displayPrizeMoney = 0
onecorrectcount = 0
while(confirmation.capitalize()!="Yes"):
  confirmation = input("Are you ready for the game ? : ")
  print("Processing...")
l1 = [
  "What is the capital of Australia?",
  "Who wrote the play “Romeo and Juliet”?",
  "Which gas is most abundant in Earth’s atmosphere?",
  "Which planet is known as the “Red Planet”?",
  "Who was the first woman to fly solo across the Atlantic Ocean?",
  "What is the chemical symbol for gold?",
  "Which country is famous for the Taj Mahal?",
  "Who painted the “Mona Lisa”?",
  "Which ocean is the largest by area?",
  "What is the currency of Japan?",
  "What is the name of Thor’s hammer?",
  "In the anime “Naruto,” what is the name of Naruto’s signature jutsu?"
     ]
l2 = [
  ["Sydney","Melbourne","Canberra","Perth"],
  ["William Shakespeare","Charles Dickens","Jane Austen","Mark Twain"],
  ["Oxygen","Nitrogen","Carbon dioxide","Hydrogen"],
  ["Venus","Mars","Jupiter","Saturn"],
  ["Amelia Earhart","Bessie Coleman","Harriet Quimby","Valentina Tereshkova"],
  ["Au","Ag","Fe","Cu"],
  ["India","Egypt","Turkey","Greece"],
  ["Vincent van Gogh","Pablo Picasso","Leonardo da Vinci","Michelangelo"],
  ["Atlantic Ocean","Indian Ocean","Pacific Ocean","Arctic Ocean"],
  ["Yen","Euro","Peso","Won"],
  ["Excalibur","Stormbreaker","Mjölnir","Gungnir"],
  ["Chidori","Shadow Clone Jutsu","Fireball Jutsu","Rasengan"]
]
l3 = [
  [False,False,True,False],
  [True,False,False,False],
  [False,True,False,False],
  [False,True,False,False],
  [True,False,False,False],
  [True,False,False,False],
  [True,False,False,False],
  [False,False,True,False],
  [False,False,True,False],  
  [True,False,False,False],
  [False,False,True,False],
  [False,False,False,True]
]
for i in l1:
  print(l1.index(i)+1,". ",i)
  print("Choose the correct option below :")
  for j in range(len(l2[l1.index(i)])):
    print(j+1,". ",l2[l1.index(i)][j])

  userans = int(input("Choose your answer by entering the correct option number : "))
  if(l3[l1.index(i)][userans-1]) is True:
    print("Correct Answer!!!")
    presentPrizeMoney = newPrizeMoney*(2**(l1.index(i)))
    print("You won : ₹",(presentPrizeMoney)," for giving the correct answer to this question.")
    displayPrizeMoney = presentPrizeMoney + displayPrizeMoney 
    onecorrectcount = 1
  else:
    print("Wrong answer.")
    if(onecorrectcount==0):
      displayPrizeMoney=0
    break
  print("--------------------------------------------------------------------------")
print("Your total winnings : ₹",displayPrizeMoney)  