#!/usr/bin/python3
import sys

print("The command line arguments are: ")
for i in sys.argv:
    print(i, end=' ')

print('\n\nThe PYTHONPATH is ', sys.path, '\n')