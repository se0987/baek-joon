import sys

###
# 스위치의 갯수
sw_num = int(input())
# 스위치의 상태, 켜져있으면 1 꺼져있으면 0
sw_onoff = list(map(int, input().split()))

stlst = []
student = int(input())  # 학생 수
for s in range(student):
    hman, hnum = map(int, input().split())
    stlst.append([hman, hnum])

for i in range(student):
    if stlst[i][0] == 1:  # 남학생
        a = b = stlst[i][1]
        while b <= sw_num:  # 배수동안 바꾸기
            sw_onoff[b - 1] = (sw_onoff[b - 1] + 1) % 2
            b += a

    else:  # 여학생
        sw_onoff[stlst[i][1] - 1] = (sw_onoff[stlst[i][1] - 1] + 1) % 2  # 현재위치 바꾸기
        a = stlst[i][1] - 2
        b = stlst[i][1]

        while a >= 0 and b < sw_num and sw_onoff[a] == sw_onoff[b]:
            sw_onoff[a] = (sw_onoff[a] + 1) % 2
            sw_onoff[b] = (sw_onoff[b] + 1) % 2
            a -= 1
            b += 1

for i in range(0, sw_num, 20):
    print(*sw_onoff[i:i+20])
