paper = [[0 for _ in range(1002)] for _ in range(1002)]
N = int(input())
for n in range(1, N+1):
    y, x, h, w = map(int, input().split())
    for i in range(y, y + h):
        for j in range(x, x + w):
            paper[i][j] = n
# print(*paper, sep='\n')

ans = {}
for i in range(1, N+1):
    ans[i] = 0

for i in range(1002):
    for j in range(1002):
        a = paper[i][j]
        if a in ans:
            ans[a] += 1


for i in range(1, N+1):
    print(ans[i])