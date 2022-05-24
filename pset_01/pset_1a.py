# -*- coding: utf-8 -*-
"""
**Solution for the MIT OCW 6.0001 pset_1a**
"""
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
monthly_saved = portion_saved*(annual_salary/12)


total_cost = float(input("Enter the cost of your dream home: "))
portion_down_payment = 0.25*total_cost

current_savings = 0
r = 0.04                #annual % return of investment
mr = r/12               #monthly % return of investment


months = 0
#There are two ways of increasing the current savings: 1. investments 2. salary


while current_savings < portion_down_payment:
    if current_savings == 0:
        current_savings = monthly_saved
    else:
        investment_returns = current_savings + current_savings*mr
        current_savings = investment_returns + monthly_saved
    
    months += 1
    
print(f'Number of months: {months}')
