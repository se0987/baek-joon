import math

# N과 K를 공백 기준으로 입력받는다
N, K = map(int, input().split())

student = [[0]*7 for _ in range(2)]    # for _ in : 의미없는 값으로 단순히 반복횟수만 채울 때
# 학년별/성별, [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]

# N번동안
for _ in range(N):
    # 성별 S(0, 1)와 학년 Y(1~6)를 공백 기준으로 입력받고, 
    S, Y = map(int, input().split())
    student[S][Y] += 1  # student의 S번 리스트의 Y 번에 값 추가

room = 0
for i in student:
    for j in i:
        room += math.ceil(j / K)

print(room)