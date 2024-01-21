import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int,input().split())

edge_list = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int,input().split())
    edge_list[a].append(b)
    edge_list[b].append(a)
for i in range(len(edge_list)):
    edge_list[i].sort()

bfs = deque()
bfs_visited = [0]*(n+1)
dfs = deque()
dfs_visited = [0]*(n+1)

#dfs
dfs.append(v)
while(dfs):
    now_node = dfs.pop()
    if dfs_visited[now_node] == 1:
        continue
    dfs_visited[now_node] = 1
    print(now_node, end=" ")
    for i in reversed(edge_list[now_node]):
        if dfs_visited[i] == 0:
            dfs.append(i)
print()
#bfs
bfs.append(v)
while(bfs):
    now_node = bfs.popleft()
    if bfs_visited[now_node] == 1:
        continue
    bfs_visited[now_node] = 1
    print(now_node, end=" ")
    for i in edge_list[now_node]:
        if bfs_visited[i] == 0:
            bfs.append(i)
