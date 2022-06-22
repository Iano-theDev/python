#!/usr/bin/python3
def func(a, b=5, c=10):
    print('a is', a,'\n' 'b is', b,'\n' 'and c is', c)
func(3, 7)
func(25, c=24)
func(c=50, a=100)