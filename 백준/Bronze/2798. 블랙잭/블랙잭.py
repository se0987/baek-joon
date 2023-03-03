N, M = map(int, input().split())
cards = list(map(int, input().split()))
mx = 0
for a in range(N):
    for b in range(a+1, N):
        for c in range(b+1, N):
            x = cards[a] + cards[b] + cards[c]
            if mx < x <= M:
                mx = x
print(mx)