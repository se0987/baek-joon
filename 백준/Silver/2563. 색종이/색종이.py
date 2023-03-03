paper = [[0 for _ in range(100)]for _ in range(100)]
for _ in range(int(input())):
    x, y = map(int, input().split())
    for i in range(y, y+10):
        for j in range(x, x+10):
            paper[i][j] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            cnt += 1

print(cnt)