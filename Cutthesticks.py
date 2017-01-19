#!/usr/bin/python

### https://www.hackerrank.com/challenges/cut-the-sticks ###


def cutting(sticks):

    longi = len(sticks)
    counter = 0
    cut = [longi]

    while(longi > counter):
        val = sticks[counter]
        while counter < len(sticks) and val == sticks[counter]:
            counter += 1
        cut.append(longi - counter)

    return cut






if __name__ == '__main__':
    n = int(input())
    a_sticks = [int(x) for x in raw_input().split()]

    a_sticks.sort()
    sol = cutting(a_sticks)
    sol.pop()

    for s in sol:
        print s