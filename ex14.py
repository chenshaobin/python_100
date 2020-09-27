#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    # Write a program that accepts a sentence
    # and calculate the number of upper case letters and lower case letters.
"""
word = input("Please enter a sentence :")
upper = sum(1 for i in word if i.isupper())
lower = sum(1 for i in word if i.islower())
print("upper case:{},lower cases:{}".format(upper, lower))
