import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):
    line = input().rstrip()
    print(line[0]+line[-1])
