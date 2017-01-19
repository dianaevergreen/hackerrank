#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,c,m = raw_input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]




    total_chocolates =  n / c

    envolturas = total_chocolates

    while envolturas / m != 0 :
        total_chocolates += envolturas / m
        envolturas = (envolturas / m) + (envolturas % m)

    print total_chocolates

