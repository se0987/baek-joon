N = int(input())
nlst = list(map(int, input().split()))
rlst = sorted(set(nlst))
print(*rlst)