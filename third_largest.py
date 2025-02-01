#!/usr/bin/env python3

# Python program to get third largest number from list.
# Doesn't sort the list. Uses looping and comparison to get the third largest number.

lst = []
for i in range(int(input("Enter number of list elements:\t"))):
    lst.append(int(input(f"Enter element at position {i + 1}:\t")))
print("List:\t", lst)

tmp = []
for i in lst:
    if len(tmp) < 3:
        tmp.append(i)
        tmp.sort()
    else:
        if i > tmp[0]:
            tmp[0] = i
        elif i > tmp[1]:
            tmp[1] = i
        elif i > tmp[2]:
            tmp[2] = i
print(f"Third largest element is {tmp[0]}.")