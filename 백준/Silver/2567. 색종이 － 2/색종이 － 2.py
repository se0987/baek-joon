paper = [[0 for _ in range(102)]] + [([0] + [0 for _ in range(100)] + [0]) for _ in range(100)] + [[0 for _ in range(102)]]
for _ in range(int(input())):
    x, y = map(int, input().split())
    for i in range(y+1, y+11):
        for j in range(x+1, x+11):
            paper[i][j] = 1
# print(*paper, sep='\n')

paper2 = list(map(list, zip(*paper)))
# print(*paper2, sep='\n')

cnt = 0
for i in range(102):
    for j in range(101):
        if paper[i][j] != paper[i][j+1]:
            cnt += 1
        if paper2[i][j] != paper2[i][j+1]:
            cnt += 1

print(cnt)