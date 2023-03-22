w, h = map(int, input().split())  # 공간 크기 가로/세로
p, q = map(int, input().split())  # 초기 좌표값
t = int(input())  # 개미가 움직일 시간

a = (p + t) % w
if ((p + t) // w)%2:
    a = w-a

b = (q + t) % h
if ((q + t) // h)%2:
    b = h-b

print(a, b)