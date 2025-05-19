# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.

import random

Rock = '''
    ------__
---'    ____)
       (_____)
       (_____)
       (____)
---.___(__)
---
'''

Paper = '''
    ------__
---'    ____)___
       _________)
       ___________)
       _________)
---.__________)
---
'''

Scissors = '''
    ------__
---'    ____)____
           ______)
        ___________)
        (____)
---.___(___)
'''

game_images=[Rock,Paper,Scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice>=0 and user_choice<=2:
    print(game_images[user_choice])

computer_choice=random.randint(0,2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice>=3 or user_choice<0:
    print("You typed an invalid number. You lose!")
elif user_choice==0 and computer_choice==2:
    print("You win!")
elif computer_choice==0 and user_choice==2:
    print("You Lose!")
elif computer_choice>user_choice:
    print('You lose!')
elif user_choice>computer_choice:
    print('You Win!')
elif computer_choice==user_choice:
    print("It's a draw")
