#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
 @name : six.py
 @brief : euler 6
 --------
 @author : INOPE <fballand.inope@gmail.com>
 @license : GPL3
"""

# --------
# Imports
# --------
import string
import sys,io,random
import locale
import math

"""

The sum of the squares of the first ten natural numbers is,
1² + 2² + ... + 10² = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 55*55 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers
and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.


"""
# --------
# definition
# --------
def main():
    """ Main function
    """
    
    sum_square = square_sum = 0
    for i in range(1, 101):
        sum_square += i**2
        #print(sum_square)
        square_sum += i
    result_square_sum = square_sum **2
    resultat = result_square_sum - sum_square
    print(resultat)          
    exit(0)
    
    
if __name__ == '__main__':
    main()
