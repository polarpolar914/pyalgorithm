import sys
input = sys.stdin.readline
price = int(input())
n = int(input())
sum = 0
for i in range(n):
    a, b = map(int, input().split())
    sum += a * b
if sum == price:
    print("Yes")
else:
    print("No")