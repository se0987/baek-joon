mapp = [list(map(int, input().split())) for _ in range(9)]

mx = 0
x = y = 0
for i in range(9):
    for j in range(9):
        if mx >= mapp[i][j]:
            continue
        else:
            mx = mapp[i][j]
            x = i
            y = j

print(mx)

print(x+1, y+1)
