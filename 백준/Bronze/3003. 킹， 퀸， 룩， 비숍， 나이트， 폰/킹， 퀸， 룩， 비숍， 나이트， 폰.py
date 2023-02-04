lst = list(map(int, input().split()))
c_lst = [1, 1, 2, 2, 2, 8]
e_lst = [0] * 6

for i in range(6):
    e_lst[i] = c_lst[i] - lst[i]

print(*e_lst)