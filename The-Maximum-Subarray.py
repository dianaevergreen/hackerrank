#!/bin/python

# code snippet illustrating input/output methods
N, K = raw_input().split()
N = int(N)
K = int(K)
C = []

numbers = raw_input()

i = 0
for number in numbers.split():
   C.append( int(number) )
   i = i+1

C.sort()

if N <= K:
    result = sum(C)

else:
    div = N / K
    rest = N % K

    result = 0


    ptr = N-1
    counter = 0
    k = K

    for i in range(div):
        while k > 0:
            result += (counter + 1) * C[ptr]
            ptr -= 1
            k -= 1
        k = K
        counter += 1


    for x in range(rest):

        result += (counter+1) * C[x]

print result
