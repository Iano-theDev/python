#!/usr/bin/python3
with open("myfile.txt") as f:
    for line in f:
        print(line, end='')
    print()
