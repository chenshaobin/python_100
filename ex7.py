#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    # Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
    # The element value in the i-th row and j-th column of the array should be i _ j.
"""
# solution1
"""
x, y = map(int, input("Please enter x and y:").split(','))
lst = []
for i in range(x):
    tmp = []
    for j in range(y):
        tmp.append(i * j)
    lst.append(tmp)

print(lst)
"""
# solution2
x, y = map(int, input("Please enter x and y:").split(','))
lst = [[i * j for j in range(y)] for i in range(x)]
print(lst)
