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


# guess(20)


def mach_guess():
    my_num=27
    comp_guess = random.randint(1, 100)
    while True:

        if my_num<comp_guess:
            print(f'Computer must guess lower than {comp_guess}')
            comp_guess=random.randint(1,comp_guess)
        elif my_num>comp_guess:
            print(f'Computer must guess higher than {comp_guess}')
            comp_guess=random.randint(comp_guess,100)
        else:
            print(f'You guessed it right, the number is indeed {my_num}')
            break
mach_guess()




