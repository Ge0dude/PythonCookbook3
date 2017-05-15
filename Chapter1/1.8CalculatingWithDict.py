#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 15 07:48:09 2017

@author: brendontucker
"""

prices = {
   'ACME': 45.23,
   'AAPL': 612.78,
   'IBM': 205.55,
   'HPQ': 37.20,
   'FB': 10.75
}

#often useful to invert teh keys and values of the dictionary 
#this can be done with the zip() function

#necessary because this doesn't do what we want, unless we're intrested in 
#lexicographic order...which would be odd for stocks

print(min(prices)) # Returns 'AAPL' 
print(max(prices)) # Returns 'IBM'

#the following is closer, but still not quite right

print(min(prices.values())) # Returns 10.75 
print(max(prices.values())) # Returns 612.78

#there are alternative methods that do work but are a bit complicated

print(min(prices, key=lambda k: prices[k])) # Returns 'FB' 
print(max(prices, key=lambda k: prices[k])) # Returns 'AAPL'

#just to understand that better...

#minVal = min(prices.values())

#to get what we really want we can invert the keys and values using zip()

min_price = min(zip(prices.values(), prices.keys())) 
# min_price is (10.75, 'FB')
max_price = max(zip(prices.values(), prices.keys())) 
# max_price is (612.78, 'AAPL')

zipEx = zip(prices.values(), prices.keys())

for x in zipEx:
    print(x)
    print('this is type', type(x))

'''returns
(10.75, 'FB')
(45.23, 'ACME')
(205.55, 'IBM')
(612.78, 'AAPL')
(37.2, 'HPQ')
'''
#minVal = min(zipEx) returns nothing because zip() returns an iterator that can
#only be consumed once... Something smells like functional programming
#here, need to look up what side-effect means

zipEx2 = list(zip(prices.values(), prices.keys()))

#that produces a more 'permanent' data structure--shouldn't be needed if you
#know what you want to do with your data

prices_sorted = sorted(zip(prices.values(), prices.keys()))

#not entirely sure why sorted can take an iterator and produce a list...
#thought sorted had to act on a list

#from Python docs 
    '''Return a new sorted list from the items in iterable.'''
#guess thats why. Really seeing the gains of sticking with one language 
# and really learning it. Makes it easier to understand data structures 
#if you know the peculiarities of the language 
