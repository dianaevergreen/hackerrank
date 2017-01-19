# Enter your code here. Read input from STDIN. Print output to STDOUT

cases = int(raw_input().strip())

for c in range(cases):
    a = set(raw_input().strip())
    b = set(raw_input().strip())

    intersection = a & b

    if len(intersection) > 0:
        print "YES"
    else:
        print "NO"
