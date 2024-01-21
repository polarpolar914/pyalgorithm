m,d = map(int,input().split())
day_cnt_list = [0, 31,28,31,30,31,30,31,31,30,31,30,31]
day_list = ['MON','TUE','WED','THU','FRI','SAT','SUN']
day_cnt = 0
for i in range(m):
    day_cnt += day_cnt_list[i]
day_cnt += d
day_cnt %= 7

print(day_list[day_cnt - 1])