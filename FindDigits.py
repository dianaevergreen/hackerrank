#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())

    arr = list(str(n))

    dicty = {}
    counter =0

    for b in arr:
        a = int(b)
        if dicty.get(a):
            counter += 1
        else:
            if a != 0 and n%a == 0:
                counter+=1
                dicty[a] = True
    print counter
