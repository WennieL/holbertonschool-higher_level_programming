#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name(12, "White")
say_my_name("Bob")
say_my_name("Bob", 1223)
say_my_name("John", "Smith")
say_my_name("Walter", "White")


try:
    say_my_name(12, "White")
except Exception as e:
    print(e)
