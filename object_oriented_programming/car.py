#!/usr/bin/python3
class Car:
    def __init__(self, brand):
        self.brand = brand
    
    def say_hi(self):
        print("Hi, i'm a {}".format(self.brand))

a = Car("Audi")
b = Car("BMW")
c = Car("Benz")

a.say_hi()
b.say_hi()
c.say_hi()