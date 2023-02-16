N = int(input())
cnt = 0

while True:
    a = N - (3 * cnt)
    if a < 0: # 나누어 떨어지지 않으면
        cnt = -1
        break
    elif a % 5 == 0: # 5로 나누어 떨어지면
        cnt += a//5
        break
    else: cnt += 1 # 3의 배수만큼 늘려가며 계산

print(cnt)