#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
 @name : five.py
 @brief : euler 5
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


2520 is the smallest number that can be divided by each
of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly
divisible by all of the numbers from 1 to 20?

"""
# --------
# definition
# --------
def main():
    """ Main function
    """
    
    result=0
    LimitFactor=20
    CurrentFactor=2 #1 is not util
    while (CurrentFactor!=LimitFactor):
        CurrentFactor=2 #one is not util
        result+=1
        while (CurrentFactor<LimitFactor):
            if result%CurrentFactor==0:
               CurrentFactor+=1 
            else:
                break
            #print(CurrentFactor)
    print(result)           
    exit(0)
    
    
if __name__ == '__main__':
    main()
