# Enter your code here. Read input from STDIN. Print output to STDOUT

cases = int(raw_input())

for c in range(cases):
    n, m = [int(x) for x in raw_input().split()]


    graph = {}
    ans = [-1]*(n+1)

    for g in range(1,n+1):
        graph[g] = set([])

    for i in range(m):
        first, second =[int(x) for x in raw_input().split()]

        graph[first].add(second)
        graph[second].add(first)


    start = int(input())
    Queue = [(start,0)]
    visited = set([start])



    while Queue:
        current, distance = Queue.pop(0)

        ans[current] = distance


        neighbors =graph[current]-visited
        Queue.extend([(z, distance + 6) for z in neighbors])
        visited.add(current)
        for n in neighbors:
            visited.add(n)


    print " ".join([str(x) for x in ans[1:] if x != 0])

