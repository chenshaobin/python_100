#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    # With a given integral number n, write a program to generate a dictionary that contains (i, i x i)
    # such that is an integral number between 1 and n (both included).
    # and then the program should print the dictionary
"""

# solution 1: use loop
"""
n = int(input("Please enter a number:"))
ans = {}
for i in range(1, n+1):
    ans[i] = i * i
print(ans)
"""
# solution 2
"""
n = int(input("Please enter a number:"))
ans = {i: i * i for i in range(1, n + 1)}
print(ans)
"""
# solution 3
try:
    n = int(input("Please enter a number:"))
except ValueError as err:
    print(err)

dictDemo = dict()
for item in range(n+1):
    if item == 0:
        continue
    else:
        dictDemo[item] = item * item

print(dictDemo)

