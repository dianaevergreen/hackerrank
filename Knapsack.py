# Enter your code here. Read input from STDIN. Print output to STDOUT


dicty = {}

def knapsack(n, k):
    matrix = [[0 for x in range(k+1)] for y in range(len(n)+1)]


    for i in range(1, len(n) + 1):
        for j in range(1, k+1):

            if n[i-1] > j:

                matrix[i][j] = matrix[i-1][j]
            else:

                matrix[i][j] = max(matrix[i-1][j], n[i-1] + matrix[i][j-n[i-1]])
    return matrix[-1][-1]





if __name__ == '__main__':
    cases = int(input())

    for c in range(cases):
        dicty = {}
        n, k = [int(x) for x in raw_input().split()]
        numbers = [int(x) for x in raw_input().split()]
        print  knapsack(numbers,k)
