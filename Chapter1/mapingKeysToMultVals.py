#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 11:55:34 2017

@author: brendontucker
"""
from collections import OrderedDict

d = {
'a' : [1, 2, 3], 'b' : [4, 5]
}

e = {
'a' : {1, 2, 3}, 'b' : {4, 5}
}

'''here choice of dict vs list has to do with whether multiple values
need to be kept, as well as order of entry. This is part of why I have a hard
time remembering what to do with dictionaries--there are many methods to choose
to alter them, depending on the internal data'''

d['a'].append(3)
# print(d['a']) -> [1, 2, 3, 3]
e['a'].add(3)
# print(e['a']) -> {1, 2, 3}

        
'''default dict can also be useful, preserves the insertion order'''

order = OrderedDict()

order['whyy'] = 12
order['second'] = 0
order['apple'] = 2
order['bananas'] = 1

for key in order:
    print(key, order[key])
