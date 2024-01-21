import sys
input = sys.stdin.readline
n, m = map(int, input().split())
numlist = [0] * n
for _ in range(m):
    a, b, c = map(int, input().split())
    numlist[a-1:b] = [c] * (b-a+1)
print(*numlist)
