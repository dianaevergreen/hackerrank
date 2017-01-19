# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

lista = [int(x) for x in raw_input().split()]

lista.sort()

mini = 100000000
ans = []

for a in range(len(lista)-1):
    if abs(lista[a] - lista[a+1]) < mini or abs(lista[a+1] - lista[a] < mini):
        ans = [lista[a], lista[a+1]]
        mini = min(abs(lista[a] - lista[a+1]), abs(lista[a+1] - lista[a]) )
    elif abs(lista[a] - lista[a+1]) == mini or abs(lista[a+1] - lista[a]) == mini:
        ans.extend([lista[a], lista[a+1]])


print " ".join(str(x) for x in ans)
