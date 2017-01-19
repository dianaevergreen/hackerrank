# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/usr/bin/python
## https://www.hackerrank.com/challenges/pangrams


def panagram(sent):
    alphabet = [0]*26

    for s in range(len(sent)):
        o = int(ord(sent[s]))

        if o > 64 and o < 91:
            a = o-65
            if alphabet[a] == 0:
                alphabet[a] = 1

        if o > 96 and o < 123:
            a = o-97
            if alphabet[a] == 0:
                alphabet[a] = 1

    for a in alphabet:
        if a != 1:
            return "not pangram"

    return "pangram"




if __name__ == '__main__':
    sentence = list(raw_input())
    print panagram(sentence)