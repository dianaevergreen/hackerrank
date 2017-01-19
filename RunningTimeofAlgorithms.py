# Enter your code here. Read input from STDIN. Print output to STDOUT

def insertionSort(ar):
    counter = 0

    for i in range(1, len(ar)):
        e = ar[i]
        flag = False
        for j in range(i-1, -1, -1):

            if ar[j] > e:
                ar[j+1] = ar[j]
                counter += 1
                ar[j] = e
            else:
                break

    print counter




    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
