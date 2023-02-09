def minmove(h_news, h_position, bilding_news, bilding_positon, map_wide, map_high):
    if h_news == bilding_news:  # 경비원과 건물의 방향이 같다면
        return abs(h_position - bilding_positon)
    # 방향이 마주보고 있다면
    elif (h_news in (1, 2) and bilding_news in (1, 2)):
        if h_news in (1, 2):  # 가로 위치 ( 1 북, 2 남, 3 서, 4 동 )
            hap1 = h_position + map_high + bilding_positon  # 왼쪽으로 갈 때
            hap2 = (map_wide - h_position) + map_high + (map_wide - bilding_positon)  # 오른쪽으로 갈 때
            if hap1 >= hap2:
                return hap2
            else:
                return hap1
    elif (h_news in (3, 4) and bilding_news in (3, 4)):
        if h_news in (3, 4):  # 세로 위치
            hap1 = h_position + map_wide + bilding_positon  # 위로 갈 때
            hap2 = (map_high - h_position) + map_wide + (map_high - bilding_positon)  # 아래로 갈 때
            if hap1 >= hap2:
                return hap2
            else:
                return hap1
    else:  # 방향이 하나 차이날 때
        if h_news == 1 or bilding_news == 1:
            if bilding_news == 3 or h_news == 3:
                return h_position + bilding_positon
            else:  # a == 4 or x == 4
                if bilding_news == 4:
                    return map_wide - h_position + bilding_positon
                else:
                    return map_wide - bilding_positon + h_position

        elif h_news == 2 or bilding_news == 2:
            if bilding_news == 3:
                return map_high - bilding_positon + h_position
            elif h_news == 3:
                return bilding_positon + map_high - h_position
            else:  # a == 4 or x == 4
                return map_wide - h_position + map_high - bilding_positon


W, H = map(int, input().split())
Bnum = int(input())

A = [0 for _ in range(Bnum)]
B = [0 for _ in range(Bnum)]

for i in range(Bnum):
    A[i], B[i] = map(int, input().split())

X, Y = map(int, input().split())

hap = 0

for j in range(Bnum):
    hap += (minmove(X, Y, A[j], B[j], W, H))
print(hap)
