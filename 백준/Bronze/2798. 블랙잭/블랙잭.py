N, M = map(int,input().split())
cards = list(map(int, input().split()))
from itertools import combinations
mx = 0
for i in combinations(cards, 3):
    if M>=sum(i) > mx:
        mx = sum(i)
print(mx)