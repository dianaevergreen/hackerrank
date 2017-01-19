#!/usr/bin/py
# Head ends here
def pairs(a,k):
    #a contains array of numbers and k is the value of difference
    answer = 0

    a.sort()

    ptr1 = 0
    ptr2 = 1

    while ptr2 < len(a):
        if a[ptr2] - a[ptr1] == k:
            answer += 1
            ptr2 += 1
        elif a[ptr2] - a[ptr1] < k:
            ptr2 += 1
        else:
            ptr1 += 1

    return answer
# Tail starts here
if __name__ == '__main__':
    a = map(int, raw_input().strip().split(" "))
    _a_size=a[0]
    _k=a[1]
    b = map(int, raw_input().strip().split(" "))
    print pairs(b,_k)
