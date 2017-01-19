#!/bin/python

import sys


time = raw_input().strip()

t = time.split(':')

if t[-1][-2:] == "AM":
    if t[0] == "12":
        print "00"+ ":" + t[1] + ":" + t[-1][:2]
    else:
        print t[0] + ":" + t[1] + ":" + t[-1][:2]
else:
    if t[0] == "12":
        print "12"+ ":" + t[1]+ ":"+ t[-1][:2]
    else:
        print str(int(t[0])+12) + ":" + t[1]+ ":"+ t[-1][:2]
