#!/usr/bin/env python3

# Python program to get common elements from two lists.
x = input('Enter elements of list 1 separated by ,\t').split(',')
y = input('Enter elements of list 2 separated by ,\t').split(',')

print(f'List 1:\t{x}')
print(f'List 2:\t{y}')

z = [i for i in x if i in y]
print(f'Common elements are {z}.')