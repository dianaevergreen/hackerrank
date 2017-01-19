# Enter your code here. Read input from STDIN. Print output to STDOUT

cases = int(raw_input())

for c in range(cases):
    s1 = raw_input()


    ptr = len(s1)-1

    flag = True
    for i in range(1,len(s1)):
        if abs(ord(s1[i]) - ord(s1[i-1])) != abs(ord(s1[ptr]) - ord(s1[ptr-1])):
            flag = False
            break
        ptr -= 1

    if flag is True:
        print "Funny"
    else:
        print "Not Funny"
