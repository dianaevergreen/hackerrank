# Enter your code here. Read input from STDIN. Print output to STDOUT


def icecream(N, M):
    sol = []

    for i in range(len(M)-1):
        for j in range(i + 1, len(M)):
            if M[i] + M[j] == N:
                sol.append((i,j))

    return sol




if __name__ == '__main__':
    cases = int(input())

    for c in range(cases):
        M = int(input())
        N = int(input())
        flavors = [int(x) for x in raw_input().split()]

        if len(flavors) == 1:
            print None

        if len(flavors) == 2:
            if sum(flavors) == N:
                print 0, 1

        else:
            sol = icecream(M, flavors)

            for s in sol:
                print s[0]+1 , s[1]+1