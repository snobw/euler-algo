#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
 @name : two.py
 @brief : euler 2
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
fibonacci
"""
# --------
# definition
# --------
def main():
    """ Main function
    """
    startPoint=0
    LimitPoint=4000000
    secondPoint=1
    result=0
    tmp=0
    #for secondPoint in stopPoint:
    while tmp<LimitPoint:
            tmp=startPoint+secondPoint
            if tmp%2 == 0: #specific euler: sum of pairs
                result=result+tmp
                print(result)
            startPoint=secondPoint
            secondPoint=tmp
            #print('\n')
            #print(tmp)
    exit(0)
    
if __name__ == '__main__':
    main()
