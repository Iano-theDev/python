#!/usr/bin/python3
class Person:
    def __init__(self, name):
        self.name = name

    
    def say_hi(self):
        print("Hello, my name is {}".format(self.name))


p = Person('Yanos')
p.say_hi()

# could have also been written as :
# Person('Yanos').say_hi()
