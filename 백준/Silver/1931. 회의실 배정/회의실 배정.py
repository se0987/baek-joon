import sys
input = sys.stdin.readline

N = int(input())
lst = []
for i in range(N):
    lst.append(list(map(int, input().split())))

lst.sort(key=lambda x:(x[1],x[0])) # 회의 끝나는 시간 순으로 정렬, 끝나는 시간이 같다면 시작 시간 순으로 정렬
# print(lst)

cnt = 1
a = lst[0][1]
for j in range(1,N):
    if a <= lst[j][0]:
        cnt += 1
        a = lst[j][1]

print(cnt)