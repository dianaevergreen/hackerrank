#!/bin/python
def partition(ar):
    l = len(ar)

    new_ar = [None] * l

    p = ar[0]

    ptr1 = 0
    ptr2 = l - 1

    for i in range(1, len(ar)):
        if ar[i] < p:
            new_ar[ptr1] = ar[i]
            ptr1 += 1
        else:
            new_ar[ptr2] = ar[i]
            ptr2 -= 1
    new_ar[ptr1] = p

    print " ".join(str(x) for x in new_ar)



    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
partition(ar)

