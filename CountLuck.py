# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/usr/bin/python
### https://www.hackerrank.com/challenges/count-luck



def magic_path(matrix, nn,mm, hermione, salida):
    Q = [hermione]


    movR = [1,-1,0,0]
    movC = [0,0,1,-1]


    while Q:
        a,b = Q[0]
        Q.pop(0)


        for mov in range(4):
            at = a + movR[mov]
            bt = b + movC[mov]
            if at >= 0 and at < nn and bt >= 0 and bt < mm:
                if matrix[at][bt] == 0:
                    matrix[at][bt] = matrix[a][b] + 1
                    Q.append([at,bt])



    t,r = hermione
    matrix[t][r] = 0
    camino = [salida]
    while camino[-1] != [t,r]:
        k,p = camino[-1]
        for mov in range(4):
            kt = k + movR[mov]
            pt = p + movC[mov]
            if kt >= 0 and kt < nn and pt >= 0 and pt < mm:
                if matrix[kt][pt] == matrix[k][p] -1 :
                    camino.append([kt,pt])
                    break
    camino.reverse()
    return camino


def waves(camino, matrix,n,m):
    movR = [1,-1,0,0]
    movC = [0,0,1,-1]

    counter = 0
    k = 0

    for c in range(1,len(camino)):
        i,j = camino[c-1]
        for mov in range(4):

            it = i + movR[mov]
            jt = j + movC[mov]
            if it < n and it >=0 and jt < m and jt >=0:
                if matrix[it][jt] == c:
                    counter += 1

        if counter > 1:
            k += 1
        counter = 0

    return k




if __name__ == '__main__':
    cases = int(input())
    for c in range(cases):
        n,m = [int(x) for x in raw_input().split()]
        matrix = []

        for nn in range(n):
            matrix.append(list(raw_input()))
        w = int(input())
        #print "waves:", w

        for nn in range(n):
            for mm in range(m):
                if matrix[nn][mm] == 'X':
                    matrix[nn][mm] = -1
                elif matrix[nn][mm] == '.':
                    matrix[nn][mm] = 0
                elif matrix[nn][mm] == '*':
                        matrix[nn][mm] = 0
                        salida = [nn,mm]
                else:
                    matrix[nn][mm] = 0
                    Hermione = [nn,mm]

        k=waves(magic_path(matrix,n,m, Hermione, salida), matrix, n,m)
        if w == k:
            print "Impressed"
        else:
            print "Oops!"

