import sys

n, m = map(int, sys.stdin.readline().split())  # 수의 개수, 합을 구해야 하는 횟수
nums = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
for p in range(n):
    for q in range(1, n):
        nums[p][q] += nums[p][q - 1]
# print(nums)

for _ in range(m):
    sum = 0
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for i in range(x1-1, x2):
        sum += nums[i][y2-1]-nums[i][y1-2] if y1 >= 2 else nums[i][y2-1]

    print(sum)