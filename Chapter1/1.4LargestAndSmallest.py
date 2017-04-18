#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 11:09:14 2017

@author: brendontucker
"""

import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

#this would've been nice to know about when I did the OHLC challenge with 
#Two Sigma...


portfolio = [
   {'name': 'IBM', 'shares': 100, 'price': 91.1},
   {'name': 'AAPL', 'shares': 50, 'price': 543.22},
   {'name': 'FB', 'shares': 200, 'price': 21.09},
   {'name': 'HPQ', 'shares': 35, 'price': 31.75},
   {'name': 'YHOO', 'shares': 45, 'price': 16.35},
   {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, portfolio, key = lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key = lambda s: s['price'])

'''nlargest and nsmallest work well when N is relatively small. When N=1 , 
min() and max() are better choices. When N is near the size of the collection
slices that have been sorted() are often more appropriate'''