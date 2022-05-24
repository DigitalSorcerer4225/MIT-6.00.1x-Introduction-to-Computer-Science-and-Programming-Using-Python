# -*- coding: utf-8 -*-
"""
@author: echoes
"""

# One number is odd
#  - then the odd number is the smallest
# Two numbers are odd
#  - find the smallest odd number between the two odd nums
# Three numbers are odd
#  - find the smallest odd number between the three odd num
# No odd numbers
#  - find the smallest number btwn the numbers
 
numbers = []

while len(numbers) < 3:
    x = int(input("Enter a number: "))
    numbers.append(x)

odd_nums = []

for x in numbers:
    if not(x%2==0):
        print(f'{x} is odd')
        odd_nums.append(x)
        
if odd_nums: #If the list contains elements then...
   largest_odd = max(odd_nums)
   print(f'The largest odd number is: {largest_odd}')
   
else:
   smallest_num = min(numbers)
   print(f'There are no odd numbers. Although the smallest number is: {smallest_num}')
    
