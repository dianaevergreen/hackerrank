# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/usr/bin/python

## Fibonacci Modified: https://www.hackerrank.com/challenges/fibonacci-modified


def fibonacci_modified(a,n):
    sol = a[:]
    for i in range(n-2):
        sol.append(sol[i] + (sol[i+1])**2)
    return sol[n-1]


if __name__ == '__main__':
    A = [int(x) for x in raw_input().split()]
    N = A.pop(-1)
    print fibonacci_modified(A,N)