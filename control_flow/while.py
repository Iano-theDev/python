#!/usr/bin/python3
number = 23
running = True

while running:
    guess = int(input('Enter an integer: '))

    if guess == number:
        print('Congratulations, you guessed it.')
        running = False
    elif guess < number:
        print('No, its a little higher than that')
    else:
        print('No, its  is a little lower than that')
else:
    print('The while loop is over')

print('Done')