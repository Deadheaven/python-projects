import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'guess a number between 1 and {x} :'))
        if guess < random_number:
            print('too low')
        elif guess > random_number:
            print('too high')

    print(f'noice , you have guessed the number {random_number}')


def compguess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(f' is the {guess} too high,too low or correct')
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'the comp guessed your number {guess}')


choice = 0
while choice != 3:
    choice = (int(input('1. You guess the number \t'
                        '2. Computer guesses the number \t 3. exit : ')))

    if choice == 1:
        guess(10)
    elif choice == 2:
        compguess(10)
