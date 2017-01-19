# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/usr/bin/python

## https://www.hackerrank.com/challenges/palindrome-index


def palindrome(sent):
    l, r = 0, len(sent)-1
    while l < r and l != r:
        if sent[l] != sent[r]:
            return False
        l += 1
        r -= 1
    return True



def index(sentence):

    left, right = 0,len(sentence)-1

    while left < right and left != right:
        if sentence[left] != sentence[right]:
            if palindrome(sentence[left:right]):
                return right
            elif palindrome(sentence[left+1:right+1]):
                return left
        left += 1
        right -= 1
    return -1




if __name__ == '__main__':
    cases = int(input())
    for c in range(cases):
        sentence = list(raw_input())
        print index(sentence)