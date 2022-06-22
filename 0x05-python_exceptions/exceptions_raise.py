#!/usr/bin/python3
class ShortInteruptException(Exception):
    '''A user defined exception class.'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('Enter something --> ')
    if len(text) < 5:
        raise ShortInteruptException(len(text), 5)
except EOFError:
    print('Why did you do an EOF on me?')
except ShortInteruptException as ex:
    print(('ShortInteruptException: The input was ' + 
            '{} characters long, expected at least {}')
            .format(ex.length, ex.atleast))
else:
    print('No exception was raised.')
