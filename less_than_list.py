#!/usr/bin/env python3

# Python program to get number less than list from list.

lst = []
for i in range(int(input("Enter number of list elements:\t"))):
    lst.append(int(input(f"Enter element at position {i + 1}:\t")))

print("List:\t", lst)

num = int(input("Enter number to compare:\t"))

less_than_list = []
for i in lst:
    if i < num:
        less_than_list.append(i)

print(f"Numbers less than {num} are {less_than_list}.")