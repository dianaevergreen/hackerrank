#!/bin/python

def partition(l):

    pivot = l[0]
    L =[]
    R = []

    for i in l[1:]:
        if i < pivot:
            L.append(i)
        else:
            R.append(i)

    return L + [pivot] + R, len(L)


def quickSort(ar):
    if len(ar) <= 1:
        return ar
    else:
        a, i_p = partition(ar)


        L = quickSort(a[:i_p])
        R = quickSort(a[i_p+1:])

        print  " ".join( str(x) for x in L + [a[i_p]] + R)
        return L + [a[i_p]] + R

    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
quickSort(ar)
