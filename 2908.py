import sys
input = sys.stdin.readline
a,b = input().split()
a,b = a[::-1], b[::-1]
a,b = int(a), int(b)
print(max(a,b))