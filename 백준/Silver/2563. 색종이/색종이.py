mapp = [[0] * 100 for _ in range(100)]
cnt = 0
T = int(input()) # 색종이 수
for tc in range(1, T + 1):
    X, Y = map(int, input().split())

    for x in range(X, X+10):
        for y in range(Y, Y+10):
            mapp[y][x] = 1

for i in range(100):
    for j in range(100):
        if mapp[i][j] == 1:
            cnt += 1

print(cnt)