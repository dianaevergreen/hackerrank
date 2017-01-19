# Enter your code here. Read input from STDIN. Print output to STDOUT

n, k = [int(x) for x in raw_input().split()]

problems = [int(x) for x in raw_input().split()]

array = [None]
special_problems = 0

for i in problems:
    if i < k:
        p1 = 1
        p2 = 0
    else:
        p1 = i / k

        if i % k > 0:
            p2 = 1
        else:
            p2 = 0

    pages = p1 + p2


    start = 1

    if i < k:
        end = i
    else:
        end = k

    for j in range(pages):
        array.append((start,end))
        start = end + 1

        if end + k > i:
            end = i
        else:
            end += k

for a in range(1,len(array)):
    s = array[a][0]
    e = array[a][1]

    if a >= s and a <= e:
        special_problems += 1

print special_problems
