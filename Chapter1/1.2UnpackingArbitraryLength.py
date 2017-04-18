#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 08:21:34 2017

@author: brendontucker
"""

'''can use Python star expressions (*expression) to accomplish this goal'''
testList = list(range(24)) 

def drop_first_last(grades): 
    first, *middle, last = grades 
    return middle
print(drop_first_last(testList))
#this does indeed drop 0 and 23, the first and last entries