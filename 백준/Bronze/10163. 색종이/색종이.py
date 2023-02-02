arr = [[0] * 1001 for _ in range(1001)]  # 빈 101 * 101 리스트
# for i in arr:
#     print(i)

T = int(input())
for ct in range(1, T + 1):  # 입력받은 색종이 수 만큼 반복
    x, y, w, h = map(int, input().split())
    for a in range(x, (x + w )):  # x1 ~ x2
        for b in range(y, (y + h )):
            arr[b][a] = ct
# print(arr)
#
# for i in arr:
#     print(i)

cnt = [0] * T  # 색종이 수 만큼 카운트 인덱스 만들기
for n in range(T):  # 색종위 수 만큼 반복
    for i in range(1001):
        for j in arr[i]:  # j가 arr[i]에 있는 항목일 때, (0~T)
            if n + 1 == j:
                cnt[n] += 1

for i in cnt:
    print(i)