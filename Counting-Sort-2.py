# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
lista = [int(x) for x in raw_input().split()]

counter_list = [0]* len(lista)

for i in lista:
    counter_list[i] += 1

for j in range(len(counter_list)):
    if counter_list[j] != 0:
        print " ".join(str(x) for x in [j] * counter_list[j]) ,
