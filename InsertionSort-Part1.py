#!/bin/python
def insertionSort(ar):
    last_e = ar[-1]
    i = 0
    for i in range(len(ar)-1, -1,-1):
        if i == 0:
            ar[i] = last_e
            print ' '.join(str(x) for x in ar)

        elif ar[i-1] > last_e:
            ar[i] = ar[i-1]
            print ' '.join(str(x) for x in ar)

        else:
            ar[i] = last_e
            print ' '.join(str(x) for x in ar)

            break




    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)

