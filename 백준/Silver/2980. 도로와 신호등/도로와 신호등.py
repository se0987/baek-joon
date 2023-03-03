N, L = map(int, input().split())
road = [[0, 0] for _ in range(L)]
for i in range(N):
    d, r, g = map(int, input().split())
    road[d] = [r, g]

cnt = 0
for i in range(L):
    cnt += 1
    if road[i][0] != 0:
        a = road[i][0] + road[i][1]
        b = cnt % a
        if b < road[i][0]:
            cnt += road[i][0]- b

print(cnt+1)