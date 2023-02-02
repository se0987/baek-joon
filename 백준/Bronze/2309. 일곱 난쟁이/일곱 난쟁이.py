N = 9  # 난쟁이들의 수
height = []  # 난쟁이들의 키
Minions = []  # 찾는 난쟁이들

for i in range(N):
    h = int(input())
    height.insert(i, h)  # height = [20, 7, 23, 19, 10, 15, 25, 8, 13]

from itertools import combinations  # 조합 함수 불러오기

for i in combinations(height, 7):  # 9개 중 7개를 뽑는다. 중복X, 순서X
    if sum(i) == 100:  # 7개의 합이 100이라면
        Minions = i  # 해당 7개는 미니언즈

minions = sorted(Minions)  # 오름차순 정렬
# 줄에 하나씩 출력
print(*minions, sep='\n')