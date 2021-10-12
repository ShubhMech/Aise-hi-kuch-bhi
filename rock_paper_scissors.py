import random
print('On Count of three, enter your choice among Rock, Paper and Scissors')
import time
value=1
time.sleep(value)
print(3)
time.sleep(value)
print(2)
time.sleep(value)
print(1)
time.sleep(value)

your_choice= (input('Your choice:')).lower()

comp_choices=['rock', 'paper','scissors']
comp_choice=random.choice(comp_choices)

def win():
    if comp_choice==your_choice:
        print('It\'s a draw')
    elif (comp_choice == 'rock' and your_choice=='paper') or (comp_choice == 'scissors' and your_choice=='rock') or (comp_choice=='paper' and your_choice=='scissors'):
        print(f'You have won as the computer put {comp_choice} and you put {your_choice}.')
    else:
        print(f'You have lost!! The computer put {comp_choice} and you put {your_choice}.')

win()
