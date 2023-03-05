def move(k, m):
    # R : 한 칸 오른쪽으로
    txt = k[0]
    num = int(k[1])
    if 'R' in m:
        if txt == 'H':
            return k
        txt = chr(ord(txt) + 1)
    # L : 한 칸 왼쪽으로
    if 'L' in m:
        if txt == 'A':
            return k
        txt = chr(ord(txt) - 1)
    # B : 한 칸 아래로
    if 'B' in m:
        if num <= 1:
            return k
        num = str(num - 1)
    # T : 한 칸 위로
    if 'T' in m:
        if num >= 8:
            return k
        num = str(num + 1)

    k = txt + str(num)
    return k


king, ston, N = input().split()
N = int(N)
for i in range(N):
    m = input()
    k1 = king

    king = move(king, m)
    if king == ston:
        ston = move(ston, m)

    if king == ston:
        king = k1

print(king, ston, sep='\n')
