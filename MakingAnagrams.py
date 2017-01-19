# Enter your code here. Read input from STDIN. Print output to STDOUT

s1 = raw_input()
s2 = raw_input()

dicty = {}


for i in s1:
    if dicty.get(i):
        dicty[i] += 1
    else:
        dicty[i] = 1

counter  = 0
for j in s2:
    if dicty.get(j):
        dicty[j] -= 1

    else:
        counter += 1

for v in dicty.values():
    counter += abs(v)

print counter




