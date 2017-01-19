#!/bin/python
def insertionSort(ar):
    for i in range(1,len(ar)):
        e = ar[i]
        for j in range(i-1, -2, -1):
            if ar[j] > e:
                ar[j+1] = ar[j]
            else:
                break

        ar[j+1] = e
        print " ".join(str(x) for x in ar)



    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
