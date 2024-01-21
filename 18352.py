import sys
import heapq
input = sys.stdin.readline

n,m,k,x = map(int, input().rstrip().split())

INF = int(1e9)
dist = [0]*(n+1)

start = x

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().rstrip().split())
    graph[a].append(b)

for i in range(1,n+1):
    dist[i] = INF

def dijkstra(start):
    global dist, graph
    q = []
    heapq.heappush(q, (0,start))
    dist[start] = 0

    while(q):
        now = heapq.heappop(q)
        if dist[now[1]] < now[0]:
            continue
        for i in graph[now[1]]:
            if dist[i] > now[0]+1:
                dist[i] = now[0]+1
                heapq.heappush(q, (dist[i],i))

dijkstra(start)

ans = []
for i in range(1,n+1):
    if dist[i] == k:
        ans.append(i)

if len(ans) == 0:
    print(-1)
else:
    for i in ans:
        print(i)
