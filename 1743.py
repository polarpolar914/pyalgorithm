import sys
input = sys.stdin.readline
from collections import deque
r, c, k = map(int, input().split())

graph = [[-1]*(c) for i in range(r)]
bfs_visited = [[0]*(c) for i in range(r)]

for i in range(k):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 0

way = [[-1,0],[0,1],[1,0],[0,-1]]

def bfs(q,w):
    global graph, way, r, c, bfs_visited
    bfs = deque()
    bfs.append([q,w])
    cnt = 0
    while(bfs):
        now = bfs.popleft()
        if bfs_visited[now[0]][now[1]] == 1:
            continue
        bfs_visited[now[0]][now[1]] = 1
        cnt += 1
        graph[now[0]][now[1]] = cnt

        for i in way:
            y,x = now[0]+i[0], now[1]+i[1]
            if y >= 0 and y < r and x >= 0 and x < c and bfs_visited[y][x] == 0 and graph[y][x] < cnt and graph[y][x] != -1:
                bfs.append([y,x])

    return cnt


ans = 0

for i in range(r):
    for j in range(c):
        if graph[i][j] == 0:
            ans = max(ans, bfs(i,j))

print(ans)