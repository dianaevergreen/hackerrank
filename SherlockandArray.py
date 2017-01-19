# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/usr/bin/python

### https://www.hackerrank.com/challenges/sherlock-and-array


def sherlock(elems):

    suma_l = [0]*len(elems)
    suma_r = [0]*len(elems)


    for e in range(len(elems)):
        if e == 0:
            suma_l[0] = elems[e]
        else:
            suma_l[e] = suma_l[e-1] + elems[e]

    for e in range(len(elems)-1,-1,-1):
        if e == len(elems)-1:
            suma_r[e] = elems[-1]
        else:
            suma_r[e] =  elems[e] + suma_r[e+1]

    if len(elems) == 1:
        return "YES"
    else:
        for e in range(1,len(elems)-1):
            if suma_l[e-1] == suma_r[e+1]:
                return "YES"
    return "NO"





if __name__ == '__main__':
    cases = int(input())

    for c in range(cases):
        no_elems = int(input())
        a_elems = [int(x) for x in raw_input().split()]
        print sherlock(a_elems)


