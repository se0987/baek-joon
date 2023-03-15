# 한번이라도 같은 반이었던 사람이 가장 많은 학생!
n = int(input())
s = [list(map(int, input().split()))for _ in range(n)]

cnt = [[] for _ in range(n)]
for i in range(5):
    for q in range(n):
        for p in range(q+1, n):
            if s[q][i] == s[p][i]:
                cnt[q].append(p)
                cnt[p].append(q)
                # print(i, cnt)
# print(cnt)
ans = []
for i in range(n):
    ans.append(len(set(cnt[i])))
# print(ans)
print(ans.index(max(ans))+1)