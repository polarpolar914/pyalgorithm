import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
input_list = ['0'+input().rstrip() for _ in range(n)]

way_list = [(1,0), (0,1), (-1,0), (0,-1)]

bfs = deque()
bfs_visited = [[0]*(n+1) for i in range(m+1)]

cnt = 0
bfs.append((0,0))

while(bfs):
    now_spot = bfs.popleft()

    if now_spot[0] == n and now_spot[1] == m:
        cnt += 1
        break
    if bfs_visited[now_spot[0]][now_spot[1]]:
        continue
    else:
        bfs_visited[now_spot[0]][now_spot[1]] = 1
        cnt += 1

    for i in way_list:
        if now_spot[0] + i[0] >= 1 and now_spot[0] + i[0] <= n and now_spot[1] + i[1] >= 1 and now_spot[1] + i[1] <= m:
            if bfs_visited[now_spot[0] + i[0]][now_spot[1] + i[1]] == 0 and  input_list[now_spot[0] + i[0]][now_spot[1] + i[1]] == 1:
                bfs.append((now_spot[0] + i[0], now_spot[1] + i[1]))

print(cnt)
