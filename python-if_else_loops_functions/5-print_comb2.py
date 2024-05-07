#!/usr/bin/python3

for num in range(0, 100):
    if num < 10:
        number = "0{}".format(num)
    else:
        number = "{}".format(num)

    if num != 99:
        print("{}{}{}".format(number, ",", " "), end="")
    else:
        print("{}".format(number))
