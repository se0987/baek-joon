minions = [int(input()) for _ in range(9)]
temp = sum(minions) - 100

a1, a2 = 0, 0

for i in minions:
    for j in minions:
        if i + j == temp:
            a1, a2 = i, j
            break

minions.remove(a1)
minions.remove(a2)

minions.sort()
print(*minions, sep='\n')