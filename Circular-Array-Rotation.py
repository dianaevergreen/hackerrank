# Enter your code here. Read input from STDIN. Print output to STDOUT

n, k , q = [int(x) for x in raw_input().split()]
arr = [int(x) for x in raw_input().split()]


if k == n or k%n == 0:
    ans = arr
else:
    ans = [None] * n
    if k > n:
        k = k % n

    for j in range(n):
        if j + k < n:
            ans[j+k] = arr[j]
        else:
            ans[(j+k)-n] = arr[j]

for i in range(q):
    indx = int(input())

    print ans[indx]

