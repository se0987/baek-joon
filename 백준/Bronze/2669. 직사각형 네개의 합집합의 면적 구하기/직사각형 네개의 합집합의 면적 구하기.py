arr = [[0] * 100 for _ in range(100)]  # 빈 100 * 100 리스트
T = 4
for ct in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1 , x2):  # x1 ~ x2
        for  y in range(y1, y2):
            arr[y][x] = 1
cnt = 0
for i in range(100):
    for j in arr[i]:
        if j == 1:
            cnt += 1

print(cnt)