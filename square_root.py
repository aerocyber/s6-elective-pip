#!/usr/bin/env python3

def sqrt(n):
    z = 1
    err = abs(n - (z * z))
    while err != 0 or err > 1.0e-20:
        z = (z + (n/z))/2
        err = abs(n - (z * z))

    return z

print("Square root is: ", sqrt(int(input("Enter number:\t"))))
