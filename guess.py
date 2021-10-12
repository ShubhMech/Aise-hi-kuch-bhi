import random
def guess(x):
    comp_guess=random.randint(1,x)
    while True:
        your_guess= int(input(f'Put your number (between 1 and {x}) here:'))
        if your_guess<comp_guess:
            print(f'Guess higher than {your_guess}')
        elif your_guess>comp_guess:
            print(f'Guess lower than {your_guess}')
        else:
            print(f'You guessed it right, the number is indeed {comp_guess}')
            break


guess(20)
