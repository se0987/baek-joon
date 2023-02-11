import sys

N = int(sys.stdin.readline())
Ndic = {}
for _ in range(N):
    i = int(sys.stdin.readline())
    try:
        Ndic[i] += 1
    except:
        Ndic[i] = 1

a = sorted(Ndic)

for i in a:
    for _ in range(Ndic[i]):
        print(i)