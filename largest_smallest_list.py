#!/usr/bin/env python3

# Python program to get largest and smallest number from list.
# Doesn't use max() and min() functions. Uses sort() to sort the list.

lst = []
for i in range(int(input("Enter number of list elements:\t"))):
    lst.append(int(input(f"Enter element at position {i + 1}:\t")))
print("List:\t", lst)
lst.sort()
print(f"Largest element is {lst[-1]} and the smallest element is {lst[0]}.")
