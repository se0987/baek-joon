N = int(input())

i = 2
while N != 1:
    if N % i == 0:  # N이 i로 나눠지면 계속 나누기
        N = N / i
        print(i)
    else:  # i로 나눠지지 않으면 i 변경
        i += 1
