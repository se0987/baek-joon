N = int(input())
nlst = [list(map(int, input().split())) for _ in range(N)]
ans = sorted(nlst, key=lambda x : (x[1], x[0]))

for i in ans:
    print(*i)
