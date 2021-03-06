#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
 @name : three.py
 @brief : euler 3
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

"""
larger prime factor
the prime factor of 13195 are 5, 7,13 and 29
what is the largest prime factor of 600851475143
"""
# --------
# definition
# --------
def main():
    """ Main function
    """
    value=600851475143
    result=0
    SommeResult=0
    FirstFactor=2
    factor=FirstFactor
    while (result>=2)or(factor<=value):
        result=value/factor
        if value%factor==0: #modulo/division euclidienne
            print('\n')
            print(factor)
            print(result)
            value=result
            factor=FirstFactor
        else:
            factor=factor+1
    exit(0)
    
if __name__ == '__main__':
    main()
