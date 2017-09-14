# coding: utf-8
#
# hw0pr2a.py
#


import random          # imports the library named random

def rps():
    user = input("Welcome to RPS, Grutors of CS5! Choose your weapon: ")
    comp = random.choice( ['rock','paper','scissors'] )
    print()

    print('the user (you) chose', user)
    print('the comp (I)   chose', comp)
    print()

# The following section includes every variable outcome, organized by R, P, S.
# User choosing 'rock'
    if user == 'rock' and comp == 'rock':
        print('Tie! Try again, nerd.')

    if user == 'rock' and comp == 'paper':
        print('Paper covers rock! Looks like I win this time!')
    
    if user == 'rock' and comp == 'scissors':
        print('UGH! You crushed my scissors! I guess you win this time...')

# User choosing 'paper'
    if user == 'paper' and comp == 'rock':
        print('You covered my rock! I guess you win this time...')
    
    if user == 'paper' and comp == 'paper':
        print('Tie! Try again, nerd.')
    
    if user == 'paper' and comp == 'scissors':
        print('Scissors cut paper! Looks like I win this time!')

# User choosing 'scissors'
    if user == 'scissors' and comp == 'rock':
        print('Rock crushes scissors! Looks like I win this time!')
    
    if user == 'scissors' and comp == 'paper':
        print('UGH! Scissors cut paper! I guess you win this time...')

    if user == 'scissors' and comp == 'scissors':
        print('Tie! Try again, nerd.')

# This section contains the variables of the first section, but with proper capitalization
# User choosing 'rock'
    if user == 'Rock' and comp == 'rock':
        print('Tie! Try again, nerd.')

    if user == 'Rock' and comp == 'paper':
        print('Paper covers rock! Looks like I win this time!')
    
    if user == 'Rock' and comp == 'scissors':
        print('UGH! You crushed my scissors! I guess you win this time...')

# User choosing 'paper'
    if user == 'Paper' and comp == 'rock':
        print('You covered my rock! I guess you win this time...')
    
    if user == 'Paper' and comp == 'paper':
        print('Tie! Try again, nerd.')
    
    if user == 'Paper' and comp == 'scissors':
        print('Scissors cut paper! Looks like I win this time!')

# User choosing 'scissors'
    if user == 'Scissors' and comp == 'rock':
        print('Rock crushes scissors! Looks like I win this time!')
    
    if user == 'Scissors' and comp == 'paper':
        print('UGH! Scissors cut paper! I guess you win this time...')

    if user == 'Scissors' and comp == 'scissors':
        print('Tie! Try again, nerd.')