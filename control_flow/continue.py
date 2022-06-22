#!/usr/bin/python3
while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    if len(s) < 3:
        print("Too small")
        continue
    else:
        print('Correct! the string length is 3 or more characters long')
        print('Done')
        break