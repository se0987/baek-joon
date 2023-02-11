A, B, V = map(int, input().split())
# A : 달팽이의 이동 거리, B : 미끄러지는 거리, V : 나무 막대의 거리

import math

move = A - B
print(math.ceil((V - A) / move)+1)