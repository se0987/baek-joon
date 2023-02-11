import sys

N = int(sys.stdin.readline())
Nlst = []
for i in range(N):
    Nlst.append((int(sys.stdin.readline())))

a = sorted(Nlst)

print(*a, sep='\n')