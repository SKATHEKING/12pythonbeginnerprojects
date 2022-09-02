import random

def guess(x):
    random_number = random.randint( 1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}:'))
        if guess < random_number :
            print('guess too low ')
        elif guess > random_number:
            print('guess too high')

    print('Congratulations you have guessed the correct number.')

#guess(5)

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c' or feedback != 'C' :
        guess = random.randint(low, high)
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C):')
        if feedback == 'H' or feedback == 'h':
            high = guess - 1
        elif feedback == 'L' or feedback == 'l':
            low = guess + 1
        elif feedback == 'c' or feedback =='C':
            print(f'Congratulations computer you have guessed the number {guess}')
            break

computer_guess(5)