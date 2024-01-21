line = input().rstrip().lower()
cnt = [0]*26
for c in line:
    cnt[ord(c)-ord('a')] += 1
result = []
maxcnt = cnt[0]
for i in range(26):
    if cnt[i] > maxcnt:
        maxcnt = cnt[i]
        result = [chr(i+ord('A'))]
    elif cnt[i] == maxcnt:
        result.append(chr(i+ord('A')))
if len(result) == 1:
    print(result[0])
else:
    print('?')
