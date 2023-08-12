#import pandas as pd
#import numpy as np
# Find out why VSC doesn't like
# the import statements.

print("Welcome to the two_sum.py file.")

number_list = {8, 6, 7, 5, 3, 0, 9}
sum = 13

def two_sum(list, sum):
    for i in list:
        for j in list:
            if (i + j == sum):
                return {i, j}
    return "Sum not found"

print(two_sum(number_list, sum))