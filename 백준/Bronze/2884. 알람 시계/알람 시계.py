H, M = map(int, input().split()) # H시 M분

reM = (M + 15) % 60
reH = H
if M - 45 < 0:
    reH = H - 1
    if reH <= 0:
        reH = (reH + 24) % 24

print(f'{reH} {reM}')
