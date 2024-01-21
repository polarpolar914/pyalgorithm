import sys
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

wedding = graph[1].copy()

for i in graph[1]:
    for j in graph[i]:
        if j not in wedding and j != 1:
            wedding.append(j)

print(len(wedding))



