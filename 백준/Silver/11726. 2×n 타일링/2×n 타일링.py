memo = [0] * 1001
memo[1] = 1
memo[2] = 2

def tile(n):
    # 메모가 저장되어 있다면
    if memo[n]:
        return memo[n]

    memo[n] = tile(n - 1) +  tile(n - 2)
    return memo[n]

n = int(input())
a = tile(n)
print(a%10007)