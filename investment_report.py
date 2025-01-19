#!/usr/bin/env python3

def report(yearly_record):
    print("Year","Invested", "Return %", sep = '\t')
    return_percent = (yearly_record[2] - yearly_record[1]) / 100
    print(yearly_record[0], f'{yearly_record[1]}\t', return_percent, sep = '\t')


records = []
for i in range(int(input('Enter number of years:\t'))):
    records.append([int(input('Enter year:\t')), float(input('Invested amount:\t')), float(input('Enter final amount:\t'))])

for i in records:
    report(i)
