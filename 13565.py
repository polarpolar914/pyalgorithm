from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int, input().split())

way = [[-1,0],[0,1],[1,0],[0,-1]]

graph = []
for _ in range(n):
    graph.append(input().rstrip())

def bfs(q,w):
    global graph, way, m, n

    bfs_queue = deque()
    bfs_visited = [[0] * m for _ in range(n)]
    bfs_queue.append([q,w])

    while(bfs_queue):
        now = bfs_queue.popleft()

        if bfs_visited[now[0]][now[1]] != 0:
            continue
        else:
            bfs_visited[now[0]][now[1]] = 1

        if now[0] == n:
            return True

        for i in way:
            y, x = now[0] + i[0], now[1] + i[1]
            if y<n and y>=0 and x<m and x>=0 and bfs_visited[y][x] == 0 and graph[y][x] == '0':
                bfs_queue.append([y,x])
    for i in range(m):
        if bfs_visited[n-1][i]:
            return True
    return False

ans = 'NO'
for i in range(m):
    if graph[0][i] == '0' and bfs(0,i):
        ans = 'YES'
        break

print(ans)