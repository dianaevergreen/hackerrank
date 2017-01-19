# Enter your code here. Read input from STDIN. Print output to STDOUT

def MCSubs(A,B):
    n = len(A)
    m = len(B)



    matrix = [[0 for x in range(n+1)] for y in range(m+1)]

    for i in range(1, m+1):
        for j in range(1,n+1):
            if B[i-1] == A[j-1]:
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                matrix[i][j] = max(matrix[i][j-1], matrix[i-1][j])


    sol = [0] * matrix[-1][-1]
    ptr = len(sol) - 1

    x,  y  = m, n





    while x > 0 and y > 0:

        if matrix[x][y] > matrix[x-1][y] and matrix[x][y] > matrix[x][y-1]:


            sol[ptr]= B[x-1]
            ptr -= 1

            x -= 1
            y -= 1


        else:
            if matrix[x][y] == matrix[x-1][y]:

                x -= 1
            else:
                y -= 1

    return sol




if __name__ == '__main__':

    n, m = [int(x) for x in raw_input().split()]

    A = [int(x) for x in raw_input().split()]
    B = [int(x) for x in raw_input().split()]

    print ' '.join(str(x) for x in MCSubs(A,B))
