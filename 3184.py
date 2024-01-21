import sys
from collections import deque
input = sys.stdin.readline

way = [[-1,0],[0,1],[1,0],[0,-1]]

r, c = map(int, input().rstrip().split())

graph = [input().rstrip() for _ in range(r)]
bfs_visited = [[0]*c for _ in range(r)]

s_live, w_live = 0, 0

def bfs(R, C):
    global r,c, bfs_visited, graph, s_live, w_live

    s_cnt, w_cnt = 0, 0

    bfs = deque()

    bfs.append([R,C])

    while(bfs):
        now = bfs.popleft()

        if bfs_visited[now[0]][now[1]] == 1:
            continue

        bfs_visited[now[0]][now[1]] = 1

        if graph[now[0]][now[1]] == 'o':
            s_cnt += 1
        elif graph[now[0]][now[1]] == 'v':
            w_cnt += 1

        for i in way:
            y, x = now[0] + i[0], now[1] + i[1]

            if y >= 0 and y < r and x >= 0 and x < c and bfs_visited[y][x] == 0 and graph[y][x] != '#':
                bfs.append([y,x])

    if s_cnt > w_cnt:
        s_live += s_cnt
    else:
        w_live += w_cnt

for i in range(r):
    for j in range(c):
        if graph[i][j] != '#' and bfs_visited[i][j] == 0:
            bfs(i,j)

print(s_live, w_live)