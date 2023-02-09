import sys

K = int(sys.stdin.readline())
mapp = [list(map(int, sys.stdin.readline().split())) for _ in range(6)]
vals = []  # 변의 길이 모음
# 변의 방향에서 동쪽은 1, 서쪽은 2, 남쪽은 3, 북쪽은 4로 나타낸다.
for i in range(6): vals.append(mapp[i][1])
mxidx = vals.index(max(vals))  # 가장 큰 값의 위치
X1 = mapp[mxidx][1]  # 큰 사각형의 가로
Y1 = ''  # 큰 사각형의 세로
X2 = ''  # 뺄 사각형의 가로
Y2 = ''  # 뺄 사각형의 세로

if mapp[(mxidx + 1) % 6][1] > mapp[(mxidx + 5) % 6][1]:  # 뒤집은 ㄱ 일 때
    Y1 = mapp[(mxidx + 1) % 6][1]
    X2 = mapp[(mxidx + 4) % 6][1]
    Y2 = mapp[(mxidx + 3) % 6][1]
else:  # ㄱ 일 때
    Y1 = mapp[(mxidx + 5) % 6][1]
    X2 = mapp[(mxidx + 2) % 6][1]
    Y2 = mapp[(mxidx + 3) % 6][1]

bigbox = X1 * Y1
smallbox = X2 * Y2
print((bigbox - smallbox) * K)
