from itertools import combinations

minions = [int(input()) for _ in range(9)]
# print(minions)

lst = set(combinations(minions, 7))
# print(lst)
for i in lst:
    if sum(i) == 100:
        a = sorted(i)
        print(*a, sep='\n')
        break