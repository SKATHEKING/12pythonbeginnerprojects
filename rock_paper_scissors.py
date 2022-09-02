import random

def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors: \t")
    computer = random.choice(['r', 's', 'p'])
    if user == computer:
        return  print('draw')

    if win(user, computer):
        return  print('You won')

    return print('You lose')
def win(player,opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p' or player == 'p' and opponent =='r'):
        return True
play()