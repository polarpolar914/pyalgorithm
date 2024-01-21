import sys
input = sys.stdin.readline
alphabet = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
line = input().rstrip()
time = 0
for i in range(len(line)):
    for j in range(len(alphabet)):
        if line[i] in alphabet[j]:
            time += j+3
print(time)