# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/usr/bin/python

def esta(l, cadena):
    return l in cadena


def gem_element(gems):
    counter =0
    for r in range(ord('a'),ord('z')+1):
        l = chr(r)
        if all([esta(l,w) for w in gems]):
            counter+=1
    return counter

if __name__ == '__main__':
    cases = int(input())
    gems = []

    for c in range(cases):
        gems.append(list(raw_input()))

    print gem_element(gems)

