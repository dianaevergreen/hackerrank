# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(raw_input().strip())

for i in xrange(t):
    n = [int(x) for x in raw_input().split()]
    counter = 0

    first  = int(n[0]**0.5)

    if first**2 < n[0]:
        first += 1

    top = n[1]

    while first**2 <= top:
        first += 1
        counter +=1


    print counter

