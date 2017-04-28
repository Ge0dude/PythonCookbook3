#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 11:55:34 2017

@author: brendontucker
"""

d = {
'a' : [1, 2, 3], 'b' : [4, 5]
}

e = {
'a' : {1, 2, 3}, 'b' : {4, 5}
}

'''here choice of dict vs list has to do with whether multiple values
need to be kept, as well as order of entry'''

d['a'].append(3)
# print(d['a']) -> [1, 2, 3, 3]
e['a'].add(3)
# print(e['a']) -> {1, 2, 3}
