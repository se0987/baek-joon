# 빙고가 되는 경우의 수 찾기 -> 가로, 세로, 대각선
bingo1 = [list(map(int, input().split())) for _ in range(5)]  # 빙고판(가로)
bingo2 = list(map(list, zip(*bingo1)))  # 빙고판(세로)

bingo3 = []
bingo4 = []
for i in range(5):
    bingo3.append(bingo1[i][i])  # \ 대각선
    bingo4.append(bingo1[i][4 - i])  # / 대각선

bingo = bingo1 + bingo2  # 빙고가 되는 모든 경우의 수
bingo.append(bingo3)  # 리스트로 추가하기 위해
bingo.append(bingo4)


# 빙고판 돌면서 숫자 선언되면 빙고판에서 숫자 삭제
# 빙고판이 빈 리스트가 되면 cnt +1, cnt == 3 일 때 종료
lst = []
for i in range(5):
    lst += list(map(int, input().split()))  # 제거할 숫자

n = 0 # 제거한 숫자의 번호
for i in lst:
    n += 1
    cnt = 0
    for j in bingo: # 빙고 리스트 순회
        if i in j:
            j.remove(i)  # 모든 빙고 리스트에서 수 지우기
        if j == []:  # 빈 리스트이면 cnt + 1
            cnt += 1

    if cnt >= 3:  # 빙고가 세개이면 종료
        break
print(n)
