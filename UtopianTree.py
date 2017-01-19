#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())

    if n == 0: print 1
    else:

        height = 1
        for a in range(1,n+1):
            if a % 2 != 0:
                height *= 2
            else:
                height += 1
        print height



