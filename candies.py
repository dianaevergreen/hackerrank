# Enter your code here. Read input from STDIN. Print output to STDOUT


def candies(ratings):
    if len(ratings) == 1:
        return 1


    candies_arr = [1] * len(ratings)

    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i-1]:
            candies_arr[i] = candies_arr[i-1] + 1

    for j in range(len(ratings)-2, -1, -1):
        if ratings[j] > ratings[j+1]:
            if candies_arr[j] <= candies_arr[j+1]:
                candies_arr[j] = candies_arr[j+1] + 1


    return sum(candies_arr)






if __name__ == '__main__':
    N = int(input())
    ratings = []

    for i in range(N):
        ratings.append(int(input()))

    print candies(ratings)
