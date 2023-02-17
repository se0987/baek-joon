def hansu(N):
    cnt = 0

    for i in range(1, N + 1):
        x = list(map(int, str(i)))  # 110 -> [1, 1, 0]
        if i < 100:
            cnt += 1
        elif i < 1000:
            if x[1] - x[0] != x[2] - x[1]:
                continue
            else:
                cnt += 1
        else:  # 1000
            if x[1] - x[0] != x[2] - x[1] or x[2] - x[1] != x[3] - x[2] :
                continue
            else:
                cnt += 1
    return cnt


N = int(input())
print(hansu(N))