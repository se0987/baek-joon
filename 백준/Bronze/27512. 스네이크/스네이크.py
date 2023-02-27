n, m = map(int, input().split())  # n 가로 m 세로
print(n * m - 1) if n * m % 2 else print(n * m)
