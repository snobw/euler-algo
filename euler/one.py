               #!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
 @name : one.py
 @brief : euler 1
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
Suite nombre
multiple of 3 and 5
sum of all the multiple of 3 or 5 below 1000
"""
# --------
# definition
# --------
def main():
    """ Main function
    """
    startPoint=0
    stopPoint=1000
    somme=0
    i=0
    while i<stopPoint:
        if(((i%3)==0) or ((i%5)==0)):
            somme=somme+i 
            print('\n')
            print(i)
        i+=1
    print('\n')
    print(somme)
    exit(0)
    
if __name__ == '__main