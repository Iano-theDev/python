#!/usr/bin/python3
number = 23
guess = int(input('Enter an integer: '))

if guess == number:
    #new block
    print('Congradulations, you guessed it')
    print('(but you do not win any prizes!)')
    #end new block
elif guess < number:
    #Another new block
    print('No its a little higher than that')
else:
    print('No, it is a little lower than that')

print('Done')