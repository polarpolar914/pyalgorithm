import sys
from collections import deque
input = sys.stdin.readline

way = [[-1,0],[0,1],[1,0],[0,-1]]

m,n = map(int, input().split())
bfs_visited = [[0]*(m) for _ in range (n)]
graph = []

for i in range(n):
    graph.append(input().rstrip())

my_ans = 0
another_ans = 0

now_team = graph[0][0]
now_cnt = 0

def bfs(q,w):
    bfs = deque()
    bfs.append([q,w])
    global n,m,bfs_visited,graph,now_team,now_cnt
    while(bfs):
        now = bfs.popleft()
        if bfs_visited[now[0]][now[1]] == 1:
            continue
        bfs_visited[now[0]][now[1]] = 1
        now_cnt += 1
        for i in way:
            y,x = now[0]+i[0], now[1]+i[1]
            if y >= 0 and y < n and x >= 0 and x < m:
                if graph[y][x] == now_team and bfs_visited[y][x] == 0:
                    bfs.append([y,x])

for i in range(n):
    for j in range(m):
        if bfs_visited[i][j] == 0:
            now_team = graph[i][j]
            bfs(i,j)
            if now_team == 'W':
                my_ans += now_cnt * now_cnt
            else:
                another_ans += now_cnt * now_cnt
            now_cnt = 0

print(my_ans, another_ans)



