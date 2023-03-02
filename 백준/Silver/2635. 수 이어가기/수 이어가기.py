n = int(input())
mx = 0
mx_lst = []

for i in range(n//2, n+1):
    x = n - i
    cnt = 3
    lst = [n, i, x]

    while x >= 0:
        i, x = x, i - x
        lst.append(x)
        cnt += 1

    if cnt > mx:
        mx = cnt-1
        mx_lst = lst[:-1]

print(mx)
print(*mx_lst)
