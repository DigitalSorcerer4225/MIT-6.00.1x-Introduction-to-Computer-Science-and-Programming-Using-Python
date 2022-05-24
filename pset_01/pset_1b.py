# -*- coding: utf-8 -*-
"""
Solution for the MIT OCW 6.0001 pset_1b
""" 
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
monthly_saved = portion_saved*(annual_salary/12)


total_cost = float(input("Enter the cost of your dream home: "))
portion_down_payment = 0.25*total_cost


semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))



current_savings = 0
r = 0.04                #annual % return of investment
mr = r/12               #monthly % return of investment


months = 0
#There are two ways of increasing the current savings: 1. investments 2. salary


while current_savings < portion_down_payment:
    if current_savings == 0:
        current_savings = monthly_saved
    elif months%6 == 0:
        annual_salary = annual_salary + annual_salary*semi_annual_raise
        monthly_saved = portion_saved*(annual_salary/12)
        
        investment_returns = current_savings*mr
        current_savings = current_savings + investment_returns + monthly_saved
    else:
        investment_returns = current_savings*mr
        current_savings = current_savings + investment_returns + monthly_saved
    
    months += 1
    
print(f'Number of months: {months}')
