n = int(input())
check = [i for i in range(1, n + 1)]
idx = 0
cnt = 1
while len(check) != 1:
   idx += cnt*cnt*cnt - 1
   idx %= len(check)
   check.pop(idx)
   cnt += 1
print(check[0])