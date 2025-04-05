#  You are going to build a Rock, Paper, Scissors game.
#  You will need to use what you have learnt about randomisation and Lists to achieve this.

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
images = [rock, paper, scissors]
user_choice = int(input("What do you want to choose: rock - 0, paper - 1, scissors - 2: \n"))
if user_choice >= 0 and user_choice <= 2:
    print(images[user_choice])
computer_choice = random.randint(0,2)
print("Computer Choose: ")
print(images[computer_choice])

if user_choice >= 3 and computer_choice < 0:
    print("Invalid input, please choose between 0,1,2")
elif user_choice == computer_choice:
    print("It is a Draw")
elif user_choice == 0 and computer_choice == 1:
    print("You Lost")
elif user_choice == 0 and computer_choice == 2:
    print("You Win !!")
elif user_choice == 1 and computer_choice == 0:
    print("You Win !!")
elif user_choice == 1 and computer_choice == 2:
    print("You Lost")
elif user_choice == 2 and computer_choice == 0:
    print("You Lost")
elif user_choice == 2 and computer_choice == 1:
    print("You Win !!")
else:
    print("There is Glitch")

