# Enter your code here. Read input from STDIN. Print output to STDOUT

cases = int(raw_input().strip())

for c in range(cases):
    string = raw_input().strip()

    if len(string) % 2 == 0:

        half = len(string) / 2

        fst_half = list(string[:half])
        snd_half = list(string[half:])

        counter = 0
        for i in range(len(fst_half)):
            if fst_half[i] in snd_half:
                snd_half.remove(fst_half[i])
            else:
                counter += 1

        print counter


    else :
        print -1

