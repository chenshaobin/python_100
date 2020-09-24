#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    # Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and
    # then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
"""
# solution1
"""
def check(x):
    # 二进制转换为十进制算法
    total, power = 0, 1
    reversed(x)
    for i in x:
        total += power * (ord(i) - 48)      # 0的assic码为48
        power *= 2
    return total % 5

data = input("Please input a sequence of comma separated 4 digit binary numbers:").split(',')
my_list = []
for i in data:
    if(check(i)) == 0:
        my_list.append(i)

print(",".join(my_list))
"""
# solutin2
def check(x):
    return int(x, 2) % 5 == 0

data = input("Please input a sequence of comma separated 4 digit binary numbers:").split(',')
data = list(filter(check, data))
print(",".join(data))
