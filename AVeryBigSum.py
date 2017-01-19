#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

suma = 0

for a in arr:
    suma += a
print suma