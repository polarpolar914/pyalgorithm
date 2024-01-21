import sys
input = sys.stdin.readline
n = int(input())
input_list = []
dp = [0] * (n+2)
for i in range(n):
    input_list.append(int(input()))
dp[0] = input_list[0]
dp[1] = max(input_list[0] + input_list[1], input_list[1])