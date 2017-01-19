# Enter your code here. Read input from STDIN. Print output to STDOUT
M = {}

def coins(change, money):
    matrix = [[0 for x in range(change + 1)] for y in range(len(money) + 1)]

    for i in range(1,len(money) + 1):
        for j in range(1, change + 1 ):
            if money[i-1] > j:
                matrix[i][j] = matrix[i-1][j]

            else:
                if money[i-1] == j:
                    matrix[i][j] = 1
                matrix[i][j] +=  matrix[i-1][j] + matrix[i][j - money[i-1]]

    return matrix[-1][-1]



if __name__ == '__main__':
    ch, l = [int(x) for x in raw_input().split()]
    numbers = [int(x) for x in raw_input().split()]
    print coins(ch, numbers)
