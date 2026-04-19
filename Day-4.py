import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)≤
      (____)
---.__(___)
"""

janken = [ rock, paper, scissors ]

janken_choice = int(input("What would you like to choose 0 for Rock, 1 for Paper, 2 for Scissors?\n"))
if janken_choice <= 0 or  janken_choice >= 2:
    print(janken[janken_choice])

computer_choice = random.randint(0, 2)
print(f"Computer chose: ")
print(janken[computer_choice])

if janken_choice > 3 or janken_choice < 0:
    print("You typed a bad number")
elif computer_choice == 2 and janken_choice == 0:
    print("You win!")
elif computer_choice > janken_choice:
    print("You lose!")
elif computer_choice == janken_choice:
    print("Draw!")
elif computer_choice == 0 and janken_choice == 2:
    print("You lose!")
elif janken_choice > computer_choice:
    print("You win!")





