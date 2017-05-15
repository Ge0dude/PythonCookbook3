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

minVal = min(prices.values())
