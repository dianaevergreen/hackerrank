#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())

    max_cant_555 = n / 3
    restante = None
    while max_cant_555 >= 0:
        restante = n - 3 * max_cant_555
        if restante % 5 == 0:
            break
        max_cant_555 -= 1
    if max_cant_555 == -1:
        print -1
    else:
        print "5" * 3 * max_cant_555 + "3" * restante



