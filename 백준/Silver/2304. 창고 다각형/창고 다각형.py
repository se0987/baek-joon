N = int(input())
nlst = [list(map(int, input().split())) for _ in range(N)]
nlst.sort()

mx = 0
idx = -1
for i in range(N):
    if mx <= nlst[i][1]:
        mx =nlst[i][1]
        idx = i
total = nlst[idx][1]

a = nlst[0][0]
b = nlst[0][1]
for n in range(idx):
    if b <= nlst[n + 1][1]:
        total += b * (nlst[n + 1][0] - a)
        a = nlst[n + 1][0]
        b = nlst[n + 1][1]

a = nlst[-1][0]
b = nlst[-1][1]
for m in range(N, idx, -1):
    if b <= nlst[m - 1][1]:
        total += b * (a - nlst[m - 1][0])
        a = nlst[m - 1][0]
        b = nlst[m - 1][1]

print(total)

