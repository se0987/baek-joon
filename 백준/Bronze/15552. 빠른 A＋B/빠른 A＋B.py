import sys

T = int(sys.stdin.readline())
for i in range(T):
    N = list(map(int, sys.stdin.readline().split()))
    print(sum(N))