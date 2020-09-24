#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    # Write a program that accepts a sequence of whitespace separated words as input
    # and prints the words after removing all duplicate words and sorting them alphanumerically.
"""
# solution1
"""
word = input("Please input a sequence of whitespace separated words:").split()  # list
for i in word:
    if word.count(i) > 1:
        word.remove(i)

word.sort()
print(" ".join(word))
"""
# solution2
"""
word = input("Please input a sequence of whitespace separated words:").split()
[word.remove(i) for i in word if word.count(i) > 1]
word.sort()
print(" ".join(word))
"""
# solution 3
word = sorted(set(input("Please input a sequence of whitespace separated words:").split()))
print(" ".join(word))
