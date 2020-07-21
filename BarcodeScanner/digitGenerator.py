import random


def randomDigitGenerator(name, price):
    barcode = name[0:2].upper()

    for i in range(15):
        barcode += str(random.randrange(1, 10))

    return barcode


print(randomDigitGenerator(input("Enter a name: "), input("Enter a price: ")))
