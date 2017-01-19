#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
   a_temp = map(int,raw_input().strip().split(' '))
   a.append(a_temp)

first_diag = 0
second_diag = 0
j = 0

for i in range(n):
    first_diag += a[i][i]
    second_diag += a[i][n-j-1]
    j += 1

print abs(first_diag - second_diag)
