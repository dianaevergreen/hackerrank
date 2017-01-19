# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/usr/bin/python

def cavity(mapa):
    length = len(mapa[0])

    for i in range(1,length-1):
        for j in range(1,length-1):
            up = mapa[i-1][j]
            down = mapa[i+1][j]
            left = mapa[i][j-1]
            right = mapa[i][j+1]

            celda = mapa[i][j]

            if celda > up and celda > down and celda > left and celda > right:
                mapa[i][j] = 'X'

    return mapa


if __name__ == '__main__':
    n = int(input())
    matrix = [0]*n
    for a in range(n):
        matrix[a] =[int(x) for x in raw_input()]

    M= cavity(matrix)

    for row in M:
        line = ""
        for col in row:
            line += str(col)
        print line
