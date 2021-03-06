#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
 @name : four.py
 @brief : euler 4
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
largest palindrome product
a palindrome number reads the same both ways. the largest palindrome made
from the product of two 2-digit numbers is 9009 =91 x 99

find the largest palindrome made from the product of two 3-digit numbers
"""
# --------
# definition
# --------
def main():
    """ Main function
    """
    
    result=0
    digit=3
    StartValue=100
    LimitValue=999
    valueFirst=100
    valueSecond=100
    previous=0
    while (valueSecond<=LimitValue):
        while (valueFirst<=LimitValue):
            #print('first value'+str(valueFirst)+'second value'+str(valueSecond))
            result=valueFirst*valueSecond
            tmp=str(result)
            if tmp == tmp[::-1]:#slice char
                if result>previous:
                    print('\n')
                    previous=result
                    print(valueFirst)
                    print(valueSecond)
                    print(result)
            valueFirst=valueFirst+1
        #print("change")
        valueFirst=StartValue
        valueSecond=valueSecond+1              
    exit(0)
    
if __name__ == '__main__':
    main()
