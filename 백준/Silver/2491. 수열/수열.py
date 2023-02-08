N = int(input()) # 수열의 크기
nlist = list(map(int, input().split()))

mx1 = mn1 = cnt = mx2 = mn2 = 1

for i in range(N-1):
    if nlist[i+1] >= nlist[i]:
        cnt += 1
        mx1 += 1
    else:
        if mx2 <= cnt:
            mx2 = cnt
            cnt = mx1 = 1
        else:
            cnt = mx1 = 1

if mx1 >= mx2:
    mx = mx1
else:
    mx = mx2

for j in range(N-1):
    if nlist[j+1] <= nlist[j]:
        cnt += 1
        mn1 += 1
    else:
        if mn2 <= cnt:
            mn2 = cnt
            cnt = mn1 = 1
        else:
            cnt = mn1 = 1

if mn1 >= mn2:
    mn = mn1
else:
    mn = mn2

if mx >= mn:
    print(mx)
else:
    print(mn)