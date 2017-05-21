#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 07:27:57 2017

@author: brendontucker
"""

'''in general it is better to name variables that represent slices, than to 
hardcode slices through indexing without creating new variables. Code becomes
much more readable this way'''

items = [0, 1, 2, 3, 4, 5, 6]
#slice object can also be used
twoToFour = slice(2,4)
#allows for
#In [167]: items[twoToFour]
#Out[167]: [2, 3]
#In [169]: items[twoToFour] = [10,11]
#now items yields Out[170]: [0, 1, 10, 11, 4, 5, 6]

'''this surely must increase the memory costs?'''

a = slice(10, 50, 2) #seeing just how object-oriented Python really is 

'''slices can also be mapped onto sequences'''

s = 'HelloWorld'
a.indices(len(s))

for i in range(*a.indices(len(s))):
    print(s[i])

