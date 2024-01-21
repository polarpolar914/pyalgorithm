import sys
input = sys.stdin.readline
n,m = map(int, input().split())
input_list = []
ans_cnt = 0
for i in range(n):
    input_list.append(input().rstrip())
# 가로
for i in range(n):
    for j in range(m-3):
        # 순서대로
        if input_list[i][j] == 'E' or input_list[i][j] == 'I':
            if input_list[i][j+3] == 'P' or input_list[i][j+3] == 'J':
                if input_list[i][j+1] == 'N' or input_list[i][j+1] == 'S':
                    if input_list[i][j+2] == 'F' or input_list[i][j+2] == 'T':
                        ans_cnt += 1
        # 역순
        if input_list[i][j+3] == 'E' or input_list[i][j+3] == 'I':
            if input_list[i][j] == 'P' or input_list[i][j] == 'J':
                if input_list[i][j+2] == 'N' or input_list[i][j+2] == 'S':
                    if input_list[i][j+1] == 'F' or input_list[i][j+1] == 'T':
                        ans_cnt += 1
# 세로
for i in range(n-3):
    for j in range(m):
        # 순서대로
        if input_list[i][j] == 'E' or input_list[i][j] == 'I':
            if input_list[i + 3][j] == 'P' or input_list[i + 3][j] == 'J':
                if input_list[i+1][j] == 'N' or input_list[i+1][j] == 'S':
                    if input_list[i+2][j] == 'F' or input_list[i+2][j] == 'T':
                            ans_cnt += 1
        # 역순
        if input_list[i+3][j] == 'E' or input_list[i+3][j] == 'I':
            if input_list[i][j] == 'P' or input_list[i][j] == 'J':
                if input_list[i+2][j] == 'N' or input_list[i+2][j] == 'S':
                    if input_list[i+1][j] == 'F' or input_list[i+1][j] == 'T':
                        ans_cnt += 1
# 대각선
for i in range(n-3):
    for j in range(m-3):
    # 좌상단 -> 우하단
        # 순서대로
        if input_list[i][j] == 'E' or input_list[i][j] == 'I':
            if input_list[i + 3][j + 3] == 'P' or input_list[i + 3][j + 3] == 'J':
                if input_list[i+1][j+1] == 'N' or input_list[i+1][j+1] == 'S':
                    if input_list[i+2][j+2] == 'F' or input_list[i+2][j+2] == 'T':
                        ans_cnt += 1
        # 역순
        if input_list[i+3][j+3] == 'E' or input_list[i+3][j+3] == 'I':
            if input_list[i][j] == 'P' or input_list[i][j] == 'J':
                if input_list[i+2][j+2] == 'N' or input_list[i+2][j+2] == 'S':
                    if input_list[i+1][j+1] == 'F' or input_list[i+1][j+1] == 'T':
                        ans_cnt += 1
    # 우상단 -> 좌하단
        # 순서대로
        if input_list[i][j+3] == 'E' or input_list[i][j+3] == 'I':
            if input_list[i + 3][j] == 'P' or input_list[i + 3][j] == 'J':
                if input_list[i+1][j+2] == 'N' or input_list[i+1][j+2] == 'S':
                    if input_list[i+2][j+1] == 'F' or input_list[i+2][j+1] == 'T':
                        ans_cnt += 1
        # 역순
        if input_list[i+3][j] == 'E' or input_list[i+3][j] == 'I':
            if input_list[i][j+3] == 'P' or input_list[i][j+3] == 'J':
                if input_list[i+2][j+1] == 'N' or input_list[i+2][j+1] == 'S':
                    if input_list[i+1][j+2] == 'F' or input_list[i+1][j+2] == 'T':
                        ans_cnt += 1

print(ans_cnt)