# Enter your code here. Read input from STDIN. Print output to STDOUT

a, b, n  = [int(x) for x in raw_input().split()]

def fib(a,b, n):
    if n <= 2:
        return b

    elif n == 3:
        return b**2 + a


    else:
        return fib(a,b,n-1)**2 + fib(a,b,n-2)


print fib(a,b,n)

