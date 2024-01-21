import sys

input = sys.stdin.readline
n = int(input())
for i in range(n):
    n, string = input().split()
    n = int(n)
    for j in range(len(string)):
        print(string[j] * n, end="")
    print()
