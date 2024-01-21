import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())

i_list = []
s_list = []
e_list = []

way = [[-2,-1],[-1,-2],[1,-2],[2,-1],[2,1],[1,2],[-1,2],[-2,1]]

for _ in range(n):
    i_list.append(int(input().rstrip()))
    s_list.append(list(map(int, input().rstrip().split())))
    e_list.append(list(map(int, input().rstrip().split())))

def bfs(i):
    size = i_list[i]
    start = s_list[i]
    end = e_list[i]

    bfs_queue = deque()
    bfs_visited = [[0]*size for _ in range(size)]

    bfs_queue.append([start[0],start[1],0])

    while(bfs_queue):
        bfs_now = bfs_queue.popleft()

        if bfs_visited[bfs_now[0]][bfs_now[1]] != 0:
            continue

        bfs_visited[bfs_now[0]][bfs_now[1]] = 1

        if bfs_now[0] == end[0] and bfs_now[1] == end[1]:
            return bfs_now[2]

        for i in way:
            y,x = bfs_now[0]+i[0], bfs_now[1]+i[1]
            if y>=0 and y<size and x>=0 and x<size and bfs_visited[y][x] == 0:
                bfs_queue.append([y,x,bfs_now[2]+1])
    return -1

for i in range(n):
    print(bfs(i))




