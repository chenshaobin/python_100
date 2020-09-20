#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    # Write a program which can compute the factorial of a given numbers.
    # The results should be printed in a comma-separated sequence on a single line.Suppose the following input is supplied to the program: 8 Then, the output should be:40320
"""
# 使用while
"""

n = int(input())
fact = 1
i = 1
while i <= n:
    fact = fact * i
    i = i + 1
print(fact)
print("------")

"""
# 使用for
"""
n = int(input())
fact = 1
for i in range(1, n+1):
    fact = fact * i
print(fact)
print("------")
"""
# 使用 Lambda函数
"""
n = int(input())
def shortFact(x): return 1 if x <= 1 else x * shortFact(x)
print(shortFact(n))
"""
# solution 4
"""
while True:
    try:
        num = int(input("Please enter a number:"))
        break
    except ValueError as err:
        print(err)

n = num
fact = 1
while num:
    fact = num * fact
    num = num - 1
print(f'the factorial of {n} is {fact}')
"""
# solution 5

from functools import reduce

def fuc(acc, item):
    return acc * item

num = int(input("Please enter one number:"))
print(reduce(fuc, range(1, num + 1), 1))
