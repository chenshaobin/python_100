#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    # Write a program which accepts a sequence of comma-separated numbers from console and generate a list
    # and a tuple which contains every number.Suppose the following input is supplied to the program
"""

listDemo = input("Please input a series of number separated by a comma:").split(',')
tupleDemo = tuple(listDemo)
print(listDemo)
print(tupleDemo)
