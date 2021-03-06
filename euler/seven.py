#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
 @name : seven.py
 @brief : euler 7
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



By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10 001st prime number?



"""
# --------
# definition
# --------
def main():
    """ Main function
    """
    Limit=10001
    i=Start=2 #1 not prime numbers
    primeQuantity=1 #for the number two
    print(i)
    while(primeQuantity!= Limit):
        for f in range(Start, i):    
            if(i%f==0):
                break
            if (f==(i-1)):
                print(i)
                primeQuantity+=1
        i+=1  
    exit(0)
    
    
if __name__ == '__main__':
    main()
