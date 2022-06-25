#!/usr/bin/python3
zoo = ('python', 'elephant', 'penguin' )
print('Number of animals in the zo0 is {}'.format(len(zoo)))

new_zoo = ('monkey', 'camel', zoo)
print ("Numberof cages in the new_zoo is {}".format(len(new_zoo)))
print("All animals in new zoo are {}".format(new_zoo))
print("Animals brought from the old zoo are {}".format(new_zoo[2]))
print("Last animal brought from old zoo is {}".format(new_zoo[2][2]))
print("Number of animals in the new zoo is {}".format(len(new_zoo)-1 + len(new_zoo[2])))
