L = int(input())  # 롤케이크 길이
cake = [0 for _ in range(L)]
N = int(input())  # 방청객 수
mk = 0
mp = 0
for i in range(1, N + 1):
    p, k = map(int, input().split())  # 방청객 i가 종이에 적어낸 수 p, k -> p부터 k조각까지
    if k-p > mk:
        mk = k-p
        mp = i
    for n in range(p - 1, k):
        if cake[n] == 0:
            cake[n] = i
print(mp)

temp = {}
for i in range(N + 1):
    temp[i] = 0

for i in range(L):
    temp[cake[i]] += 1
# print(cake)
# print(temp)

ans = sorted(temp.items(), key=lambda x:-x[1])
# print(ans)
if ans[0][0] == 0:
    print(ans[1][0])
else:
    print(ans[0][0])