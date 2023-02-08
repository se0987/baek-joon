import sys

N, K = map(int, sys.stdin.readline().split())
# N = 온도를 측정한 날짜의수, K = 연속적인 날짜의 기간
nlist = list(map(int, sys.stdin.readline().split())) # 측정한 온도 리스트

max = hap = sum(nlist[:K])

for i in range(N-K):
    # 연속적인 며칠 동안의 온도의 합이 가장 큰 값
    hap = hap-nlist[i]+nlist[i+K]

    if hap >= max:
        max = hap


print(max)