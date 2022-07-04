#!/usr/bin/python3
class Car:
    def __init__(self, brand):
        self.brand = brand
    
    def say_hi(self):
        print("Hi, i'm a {}".format(Audi.brand))

a = Car("Audi")
b = Car("BMW")
c = Car("Benz")
Audi.say_hi()
