n = int(input())
dice = []
for _ in range(n):
    A, B, C, D, E, F = map(int, input().split())
    dice.append([A, B, C, F, D, E])

mx = 0
for i in range(1, 7): # 첫번째 주사위 윗면
    hap = 0
    a = i
    # a와 a의 맞은편 제거, hap += max값

    for j in range(n): # 모든 주사위 돌기
        lst = [1, 2, 3, 4, 5, 6] # 주사위 리셋
        # 다음 주사위에서 a와, a 맞은편 제거, hap += max값
        lst.remove(a) # 아랫면 제거
        a = dice[j][dice[j].index(a) + 3] if dice[j].index(a) < 3 else dice[j][dice[j].index(a) - 3] #위 값으로 갱신
        lst.remove(a) # 윗면 제거
        hap += lst[-1] # 남은 수 중 최대값

    if hap > mx:
        mx = hap
print(mx)