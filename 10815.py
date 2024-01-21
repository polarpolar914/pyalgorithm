import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int,input().split()))
m = int(input())
m_list = list(map(int,input().split()))

check_list = [0]*20000000

for i in n_list:
    check_list[i+10000000] = 1
for i in m_list:
    if check_list[i+10000000] != 0:
        print(1,end=" ")
    else:
        print(0, end=" ")
