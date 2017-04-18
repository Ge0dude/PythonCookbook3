#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 08:07:33 2017

@author: brendontucker
"""
#simplest version possible
p = (4,5)
x,y = p
#spacing doesn't matter, this works equally well
q = (1 ,2)
a, b = q

'''works for any Python iterable as long as the number of variables matches the
sequence length'''

data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
name, shares, price, date = data

#again, works for any iterable, pretty neat for strings
s = 'Hello'
a, b, c, d, e = s