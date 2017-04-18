#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 08:21:34 2017

@author: brendontucker

this section seems really useful for data processing, especially for 
really ugle data
"""


'''can use Python star expressions (*expression) to accomplish this goal'''
testList = list(range(24)) 

def drop_first_last(grades): 
    first, *middle, last = grades 
    return middle
print(drop_first_last(testList))
#this does indeed drop 0 and 23, the first and last entries

#also works to grab an unknown amount of ending characters
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phoneNumbers = record
#in this code, phoneNumbers will always be a list 

#works for dealing with the front end of a section of data also
testList2 = list(range(10))
*begining, nextToLast, last = testList2

'''Discussion--need to work through this because I don't quite get it yet'''

records = [
         ('foo', 1, 2),
         ('bar', 'hello'),
         ('foo', 3, 4),
         ]
    
def do_foo(x, y): 
    print('foo', x, y)
    

def do_bar(s): 
    print('bar', s)
    
for tag, *args in records: 
    if tag == 'foo':
        do_foo(*args) 
    elif tag == 'bar':
        do_bar(*args)
        
#ah, okay, just allowing for more variation in printing of unequal len data

'''again, super impressive what these star expressions can do with strings'''

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
    
    
    
    