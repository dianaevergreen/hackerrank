string = list(raw_input())

#found = False
# Write the code to find the required palindrome and then assign the variable 'found' a value of True or False

impar = 0

found = True
a = set()
for i in range(len(string)):
    current = string[i]
    if current not in a:
        a.add(current)
        occ = string.count(current)

        if occ % 2 != 0:
            if impar < 1:
                impar += 1
            else:
                found = False


if not found:
    print("NO")
else:
    print("YES")
