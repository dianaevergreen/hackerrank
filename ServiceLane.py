# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/usr/bin/python

## https://www.hackerrank.com/challenges/service-lane

if __name__ == '__main__':
    f, cases = [int(x) for x in raw_input().split()]


    freeway = [int(x) for x in raw_input().split()]

    ones = [0]* (len(freeway) + 1)
    twos = [0] * (len(freeway) + 1)
    threes = [0] * (len(freeway) + 1)

    for a in range(1,len(freeway)+1):
        if a == 1:
            if freeway[a-1] == 1:
                ones[a] = 1

            elif freeway[a-1] == 2:
                twos[a] = 1
            else:
                threes[a] = 1
        else:
            if freeway[a-1] == 1:
                ones[a] = ones[a-1] + 1
            else:
                ones[a] = ones[a-1]
            if freeway[a-1] == 2:
                twos[a] = twos[a-1] + 1
            else:
                twos[a] = twos[a-1]
            if freeway[a-1] == 3:
                threes[a] =  threes[a-1] + 1
            else:
                threes[a] = threes[a-1]


    for c in range(cases):
        i,j = [int(x) for x in raw_input().split()]
        if ones[j+1] - ones[i] > 0:
            print "1"
        elif twos[j+1] - twos[i] > 0:
            print "2"
        elif threes[j+1] - threes[i] > 0:
            print "3"

