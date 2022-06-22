#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n = len(argv) - 1
    if n == 0:
        print("0 arguments.", end='')
    elif n == 1:
        print("1 argument:", '\n', end='')
    else:
        print("{} arguments:".format(n), '\n', end='')
    for i in range(len(argv[1:])):
        print("{}: {}".format(i + 1, argv[i + 1], end=''))
