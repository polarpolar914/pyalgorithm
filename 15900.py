import sys

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 리프 노드에서 루트 노드까지의 거리들의 총 합을 구한다.
dfs = []
dfs_visited = [0]*(n+1)
dfs.append(1)
distance = [0]*(n+1)
is_leaf = [0]*(n+1)
sum_distance = 0

while(dfs):
    now_node = dfs.pop()
    if dfs_visited[now_node] == 1:
        continue
    if len(graph[now_node]) == 1:
        is_leaf[now_node] = 1
        sum_distance += distance[now_node]
    dfs_visited[now_node] = 1
    for i in graph[now_node]:
        if dfs_visited[i] == 0:
            dfs.append(i)
            distance[i] = distance[now_node] + 1

if sum_distance % 2 == 0:
    print("No")
else:
    print("Yes")