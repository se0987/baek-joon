from itertools import combinations
N = int(input())
nlist = (i for i in range(1, N+1))
cnt = 0
for i in combinations(nlist,2):
    a, b = i[0], i[1]
    if a*b <= N:
        cnt += 1

for i in range(1, N+1):
    if i**2 <= N:
        cnt += 1

print(cnt)