#!/usr/bin/env python3

binary = input("Enter binary:\t")[::-1]
decimal = 0

for i in range(len(binary)):
    decimal += int(binary[i]) * (2 ** i)

print("Decimal:\t", str(decimal))
