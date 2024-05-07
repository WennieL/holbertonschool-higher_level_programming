#!/usr/bin/python3

for num in range(0, 10):
    print("{:02}".format(num), end=", ")

for num in range(10, 90):
    if str(num)[0] != str(num)[1] and str(num)[0] < str(num)[1]:
        if num != 89:
            print("{:02}".format(num), end=", ")
        else:
            print("{:02}".format(num))
