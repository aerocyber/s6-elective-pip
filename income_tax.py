#!/usr/bin/env python3

income = float(input("Enter income:\t"))

tax_percent = 0.0

# Follows the new regime
# Slab data from: https://www.maxlifeinsurance.com/blog/tax-savings/income-tax-slab-2023-24
if income < 300000:
    tax_percent = 0.0
elif income > 300000 and income <= 600000:
    tax_percent = 6.0
elif income > 600000 and income <= 900000:
    tax_percent = 10.0
elif income > 900000 and income <= 1200000:
    tax_percent = 15.0
elif income > 1200000 and income <= 1500000:
    tax_percent = 20.0
else:
    tax_percent = 30.0

tax_payable = income * tax_percent
print("Amount to be paid as income tax:\t ", tax_payable)
