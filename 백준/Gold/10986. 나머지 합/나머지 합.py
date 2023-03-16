import sys

N, M = map(int, sys.stdin.readline().split())  # 수의 개수, 합을 구해야 하는 횟수
num = list(map(int, sys.stdin.readline().split()))  # 숫자들

# 누적합의 나머지를 저장할 배열 선언
sum = 0
renum = [0] * M

# 누적합의을 구하고 바로 나머지 수 인덱스에 값을 증가
for i in range(N):
    sum += num[i]
    renum[sum % M] += 1

# 첫 결과에 나머지가 0인 값을 집어 넣는 이유는 나머지가 0인 값들은 2개의 수를 뽑지 않아도 0으로 나누어 떨어지는 구간이기 때문
result = renum[0]

# 누적합 3,6,9 구간은 2개를 뽑지 않아도 0으로 나누어 떨어진다.
# 나머지가 같은 구간 두개를 뽑는다.
for i in renum:
    result += i * (i - 1) // 2

print(result)
