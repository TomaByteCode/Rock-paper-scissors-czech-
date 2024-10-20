import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''


paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''


scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
computerScore = 0
score = 0
all_list = [rock , paper , scissors]
while True:
    userChoose = int(input("Co si vyberete : pokud kámen napište 0 pro papír 1 a pro nůžky 2\n"))
    userPicture = all_list[userChoose]

    computerChoose = random.randint(0 , 2)
    computerPicture = all_list[computerChoose]

    print(f"Uživatel si vybral: {userPicture}")

    print(f"Počítač si vybral: {computerPicture}")

    if userChoose == computerChoose:
        print("Remíza")
    elif userChoose == 0 and computerChoose == 1:
        print("Prohrál jsi , počítač výhral!")
        computerScore += 1
    elif userChoose == 0 and computerChoose == 2:
        print("Výhral jsi , počítač prohrál!")
        score += 1 
    elif userChoose == 1 and computerChoose == 0:
        print("Výhral jsi , počítač prohrál!")
        score += 1
    elif userChoose == 1 and computerChoose == 2:
        print("Prohrál  jsi , počítač výhral!")
    elif userChoose == 2 and computerChoose == 0:
        print("Počítač výhral , prohrál jsi!")
        computerScore += 1
    elif userChoose == 2 and computerChoose == 1:
        print("Výhral jsi , počítač prohrál!")
        score += 1
    print(f"Uživatel má {score} bodu.")
    print(f"Počítač má {computerScore} bodu.")
        