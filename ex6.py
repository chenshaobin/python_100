#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    # Write a program that calculates and prints the value according to the given formula:
    # Q = Square root of [(2 *C*D)/H]
    # D is the variable whose values should be input to your program in a comma-separated sequence.
    # The output should be a string
"""
from math import sqrt

C, H = 50, 30


def calc(D):
    return sqrt((2*D*C)/H)


D = input("Please input a series of number separated by a comma:").split(',')
D = [str(round(calc(int(i)))) for i in D]   # round函数将值取整
print(",".join(D))  # 转化为以逗号为分隔符，将D所有元素合并成一个新的字符串
