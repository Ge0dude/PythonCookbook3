#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 16 06:20:12 2017

@author: brendontucker
"""

a = [1, 5, 2, 1, 9, 1, 5, 10]

def dedupe(items): 
    seen = set()
    for item in items:
        if item not in seen:
            yield item 
            seen.add(item)
                

'''yield is useful here because it we are working with a generator, which 
means we can't use return. Useful when there are large amounts of data that
only need to be accessed one time. Generators are like iterables but can only
be accessed one time and are not stored in memory '''
            
            
aPrime = list(dedupe(a))

'''this works well for items that can be hashed--which I believe allows
constant time access for lookups, not sure'''

#can be made to work with unhashable types, like dict in this example
def dedupe2(items, key=None): 
    seen = set()
    for item in items:
        val = item if key is None else key(item) 
        if val not in seen:
            yield item 
            seen.add(val)
            
a2 = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]

aPrime2 = list(dedupe(a, key=lambda d: (d['x'],d['y']))) 
#don't really understand why we need a lambda here
#understand the result and teh underlying set operation but not the mechanics
#of the lambda function







