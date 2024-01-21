import sys

input = sys.stdin.readline

n = int(input().rstrip())
input_list = list(map(int, input().rstrip().split()))

dp = [int(1e9)] * (n + 200)
dp[1] = 0

for idx, val in enumerate(input_list):
    for update_range in range(idx+2, idx+1+val+1):
        dp[update_range] = min(dp[update_range],dp[idx+1]+1)

if dp[n] == int(1e9):
    print(-1)
else:
    print(dp[n])