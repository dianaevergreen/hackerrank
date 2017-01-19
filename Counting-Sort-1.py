# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

lista = [int(x) for x in raw_input().split()]
dicty ={}

for d in range(100):
    dicty[d] = 0

for l in lista:
    dicty[l] += 1

for v in dicty.values():
    print v,