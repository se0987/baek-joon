N = int(input())  # 학생의 수
B = list(map(int, input().split()))  # 학생들이 뽑은 번호
stand = []

for i in range(N):
    if B[i] == 0:
        stand.insert(i, i + 1)  # i번 인덱스에 i+1 값을 넣겠다.
    elif B[i] > 0:  # i = 1: 2번이 1을 뽑으면, [0]에 2를 넣어야 함
        stand.insert(i - B[i], i + 1)  # i-B[i]번 인덱스에 i 값을 넣겠다.

print(*stand)