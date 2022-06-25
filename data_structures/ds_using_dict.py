#!/usr/bin/python3
# help(dict) for methods on dictionary DS in python
ab = {
    "Swaroop": "swaroop@gmail.com",
    "Larry": "larry@gmail.com",
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}

print("swaroop's address is", ab['Swaroop'])

del ab['Spammer']

print("\n There are {} contacts in the address-book\n".format(len(ab)))

for name, address in ab.items():
    print("Email of {} is {}".format(name, address))

# Adding a key-value pair
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("\nGuido's address is {}".format(ab['Guido']))
