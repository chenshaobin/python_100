#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    # Define a class which has at least two methods:
    # getString: to get a string from console input
    # printString: to print the string in upper case.
    # Also please include simple test function to test the class methods.
"""


class IoString():
    def get_string(self):
        self.s = input("Please enter one string:")

    def print_string(self):
        print(self.s.upper())

textIO = IoString()
textIO.get_string()
textIO.print_string()