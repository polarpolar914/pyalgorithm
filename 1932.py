import sys
input = sys.stdin.readline
n = int(input())
input_list = [[0]]* (n+1)

# 입력
for i in range(n):
    input_list[i] = list(map(int,input().split()))+[0]
input_list[n] = [0]*(n+1)

# dp - 트리의 말단노드부터 최상단 부모노드까지 계산
for i in range(n-1,0,-1):
    for j in range(i):
        if input_list[i][j] < input_list[i][j+1]:
            input_list[i-1][j] += input_list[i][j+1]
        else:
            input_list[i - 1][j] += input_list[i][j]
print(input_list[0][0])

