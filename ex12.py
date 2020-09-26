#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    # Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
    # The numbers obtained should be printed in a comma-separated sequence on a single line.
"""
# solution 1
"""
my_list = []
for i in range(1000, 3001):
    flag = 1
    for j in str(i):
        if ord(j) % 2 != 0:
            flag = 0
    if flag == 1:
        my_list.append(str(i))

print(','.join(my_list))
"""
# solution2
def check(element):
    return all(ord(i) % 2 ==0 for i in element)     # all returns True if all digits i is even in element

my_list = [str(i) for i in range(1000, 3001)]
my_list = list(filter(check, my_list))
print(','.join(my_list))

