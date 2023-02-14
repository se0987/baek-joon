N = int(input())
point = [0] * 301
dp = [0] * 301

for i in range(N):
    point[i] = int(input())

dp[0] = point[0]
dp[1] = max(point[1] + point[0], point[1])
dp[2] = max(point[0] + point[2], point[1] + point[2])

for i in range(3, N):
    dp[i] = max(dp[i-3] + point[i-1] + point[i], dp[i-2]+point[i])

print(dp[N-1])