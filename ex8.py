#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    # Write a program that accepts a comma separated sequence of words as input
    # and prints the words in a comma-separated sequence after sorting them alphabetically.
"""

# solution1：
"""
listDemo = input("Please enter a sequence of words:").split(',')
listDemo.sort()
print(",".join(listDemo))
"""
# solution2

def my_func(e):
    # 返回第一个字母
    return e[0]

my_list = input("Enter a comma separated string:").split(',')
my_list.sort(key=my_func)
print(','.join(my_list))

