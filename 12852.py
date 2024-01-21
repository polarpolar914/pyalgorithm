import sys
input = sys.stdin.readline

n = int(input().rstrip())

dp = [0,[]]*1000001

dp[1] = [0,[1]]
dp[2] = [1,[1,2]]
dp[3] = [1,[1,3]]

for i in range(4,n+1):
    dp[i] = [dp[i-1][0]+1,dp[i-1][1]+[i]]

    if i%2 == 0 and dp[i//2][0]+1 < dp[i][0]:
        dp[i] = [dp[i//2][0]+1,dp[i//2][1]+[i]]

    if i%3 == 0 and dp[i//3][0]+1 < dp[i][0]:
        dp[i] = [dp[i//3][0]+1,dp[i//3][1]+[i]]

print(dp[n][0])
print(*dp[n][1][::-1])