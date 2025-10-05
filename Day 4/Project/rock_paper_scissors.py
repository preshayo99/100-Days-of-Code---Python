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
---'    ____)____
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

import random

print("\nWelcome to Rock, Paper, Scissors!")

user_choice = int(input('\nWhat do you choose? Type 0 for rock, 1 for paper or 2 for scissors: '))
options = [rock, paper, scissors]

if user_choice > 2 or user_choice < 0:    
    print("Invalid input! You must enter 0, 1, or 2.")
else:
    print(f'\nYou chose:\n{options[user_choice]}')

    computer_choice = random.randint(0, 2)
    print(f"Computer chose:\n{options[computer_choice]}")

    if user_choice == computer_choice:
        print("A draw\n")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose!")