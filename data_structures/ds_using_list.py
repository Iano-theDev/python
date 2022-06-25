#!/usr/bin/python3
# This is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']

print("I have {} items to purchase".format(len(shoplist)))
print("These items are: ", end="")
for item in shoplist:
    print("{}".format(item), end=" ")
print("\nI also have to buy rice.")
shoplist.append('rice')
print("My shopping list is now {}".format(shoplist))

print("I will now sort my list")
shoplist.sort()
print("Sorted list is now {}".format(shoplist))

print("The first item i will buy is {}".format(shoplist[0]))
olditem = shoplist[0]
del shoplist[0]

print("I bought the {}".format(olditem))
print("My shopping list is now {}".format(shoplist))