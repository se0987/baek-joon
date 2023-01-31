# 첫째 줄에 정수의 개수 N 입력
N = int(input())

# 둘째 줄에는 N개의 정수를 공백으로 구분해서 입력
n = list(map(int, input().split()))

print(min(n), max(n))