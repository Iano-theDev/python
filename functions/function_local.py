#!/usr/bin/python3
x = 50

def func(x):
    print('x is ', x)
    x = 2
    print('Changed local x to', x)

func(x)
print('x is still', x)