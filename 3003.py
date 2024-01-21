ans_cnt = [1,1,2,2,2,8]
input_cnt = list(map(int, input().split()))
for i in range(6):
    print(ans_cnt[i] - input_cnt[i], end=" ")