import sys
from collections import deque
input = sys.stdin.readline
f, s, g, u, d = map(int, input().split())
visited = [0]*(f+1)
way = [u, -d]
ans = -1

def bfs(q):
    global f, s, g, u, d, visited, way, ans
    bfs = deque()
    bfs.append(q)
    visited[q] = 1
    while(bfs):
        now = bfs.popleft()
        if now == g:
            ans = visited[now] - 1
            return
        for i in way:
            y = now + i
            if y >= 1 and y <= f and visited[y] == 0:
                bfs.append(y)
                visited[y] = visited[now] + 1

bfs(s)
if ans == -1:
    print('use the stairs')
else:
    print(ans)