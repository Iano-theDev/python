#!/usr/bin/python3
def total(a, b, c, *numbers, **phonebook):
    print('a', a)

    # iterate through all the items in the tuple
    for single_item in numbers:
        print('Single_item', single_item)
    print('b', b)
    print('c', c)
    #iterate through all the items in the dictionary
    for first_part, second_part in phonebook.items():
        print(first_part,second_part)

total(1,2,3,4,6,7,5,'ian',ian=254,Jack=1123,John=2231,Inge=1560)