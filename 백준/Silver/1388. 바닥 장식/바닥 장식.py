# 1388 바닥장식
N, M = map(int, input().split())  # 세로, 가로
mapp = [list(input() + '|') for _ in range(N)] + [['-' for _ in range(M + 1)]]
cnt = 0

# '-'
for i in range(N):
    for j in range(M):
        if mapp[i][j] == '-' != mapp[i][j + 1]:
            cnt += 1

# '|'
for j in range(M):
    for i in range(N):
        if mapp[i][j] == '|' != mapp[i + 1][j]:
            cnt += 1

print(cnt)