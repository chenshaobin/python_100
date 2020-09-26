#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    # Write a program that accepts a sentence and calculate the number of letters and digits.
"""
# solution1
"""
word = input("Please enter a sentence:")
letter, digit = 0, 0
for i in word:
    if('a' <= i and i <= 'z') or ('A' <= i and i <= 'Z'):
        letter += 1
    if '0' <= i and i <= '9':
        digit += 1

print("letters: {},digits:{}".format(letter, digit))
"""
# solution2
word = input("Please enter a sentence:")
letter, digit = 0, 0
for i in word:
    if i.isalpha():
        letter += 1
    if i.isdigit():
        digit += 1

print("letters: {},digits:{}".format(letter, digit))
