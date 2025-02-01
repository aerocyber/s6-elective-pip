#!/usr/bin/env python3

# Python program to get even numbers from list.

lst = []
for i in range(int(input("Enter number of list elements:\t"))):
    lst.append(int(input(f"Enter element at position {i + 1}:\t")))
print("List:\t", lst)

even_list = [x for x in lst if x % 2 == 0]
print(f"Even numbers are {even_list}.")