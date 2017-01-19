# Enter your code here. Read input from STDIN. Print output to STDOUT

cases = int(raw_input().strip())

for c in range(cases):
    word = raw_input().strip()

    ptr1 = 0
    ptr2 = len(word)-1

    counter = 0
    while ptr1 != ptr2 and ptr1 < ptr2:
        mini = min(ord(word[ptr1]), ord(word[ptr2]))
        maxi = max(ord(word[ptr1]), ord(word[ptr2]))

        counter += maxi - mini
        ptr1 += 1
        ptr2 -= 1
    print counter