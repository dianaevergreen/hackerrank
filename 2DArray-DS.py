#!/bin/python

import sys


arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)

current_hourglass = None
max_hourglass = None

for i in range(6):
    for j in range(6):
        if i + 2 < 6 and j + 2 < 6:
            current_hourglass = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]

            if current_hourglass > max_hourglass:
                max_hourglass = current_hourglass
print max_hourglass


