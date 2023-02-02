sub = []
not_sub = []
for i in range(28):
    sub.insert(i, int(input()))

for s in range(1, 31):
    if s in sub:
        pass
    else:
        not_sub.append(s)

for i in not_sub:
    print(i)