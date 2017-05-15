#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 16 05:51:19 2017

@author: brendontucker
"""

a={
'x' : 1,
'y' : 2,
'z' : 3 
}

b={
'w' : 10,
'x' : 11,
'y' : 2 
}

# Find keys in common
a.keys() & b.keys() 
# { 'x', 'y' }

'''order shouldn't matter in this one, correct?'''

b.keys() & a.keys() 
# { 'x', 'y' } , correct, returns the exact same 

# Find keys in a that are not in b 
a.keys() - b.keys() 
# { 'z' }

# Find keys in b that are not in a
b.keys() - a.keys()
# {'w'}

# Find (key,value) pairs in common 
a.items() & b.items() # { ('y', 2) }




