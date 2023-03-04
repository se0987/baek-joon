H, W = map(int, input().split())  # H 세로 × W 가로
sky = [input() for _ in range(H)]  # 구름 'c' , 없다면 '.'

cloud = [[-1 for _ in range(W)] for _ in range(H)]
for i in range(H):
    for j in range(W):
        if sky[i][j] == 'c':
            cloud[i][j] = 0
        else:  # 현재 상태가 구름이 아니라면
            if j - 1 >= 0 and cloud[i][j - 1] != -1:  # 현재 위치가 서쪽 끝이 아니고 앞에 구름이 온다면
                cloud[i][j] = cloud[i][j - 1] + 1
for i in cloud:
    print(*i)