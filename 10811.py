import sys
input = sys.stdin.readline
n, m = map(int, input().split())
numlist = [i for i in range(1, n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    if a == b:
        continue
    numlist[a-1:b] = numlist[a-1:b][::-1]
print(*numlist)
