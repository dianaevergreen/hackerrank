#!/bin/python

import sys


n = int(raw_input().strip())
s = raw_input().strip()
k = int(raw_input().strip())

res = ""
if k >= 26 :
    k = k %26

for i in range(len(s)):
    if s[i].isalpha():
        if s[i].isupper():
            if ord(s[i]) + k <= 90:
                res += chr(ord(s[i]) + k)
            else:
                res += chr(ord(s[i]) + k - 90 +64)

        else:

            if ord(s[i]) + k <= 122:
                res += chr(ord(s[i]) + k)
            else:
                res += chr(ord(s[i]) + k - 122 + 96)


    else:
        res += s[i]
print res




