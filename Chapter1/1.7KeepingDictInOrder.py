#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 15 07:38:31 2017

@author: brendontucker
"""

from collections import OrderedDict

d = OrderedDict()
d['grok'] = 4
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3


for key in d: 
    print(key, d[key])
    
'''is built through a doubly linked list. Keys are ordered via insertion
order. When a key is first inserted, it is placed at the end of the list,
subsequent reorganization doesn't alter this order. This form of storage 
does create a larger amount of data, something like twice that of a typical
dictionary.'''