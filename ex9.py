#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    # Write a program that accepts sequence of lines as input
    # and prints the lines after making all characters in the sentence capitalized.
"""
# solution1
"""
lst = []
while True:
    x = input("Please enter one word:")
    if len(x) == 0:
        break
    lst.append(x.upper())

for line in lst:
    print(line)
"""
# solution2
def userInput():
    while True:
        s = input("Please enter one word:")
        if not s:
            return
        yield s

for line in map(lambda x: x.upper(), userInput()):
    print(line)
