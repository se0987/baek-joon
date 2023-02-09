T = int(input())
for tc in range(T):
    R, S = map(str, input().split())  # R = 반복횟수, S= 문자열
    R = int(R)
    S = list(S) #['A', 'B', 'C']

    result = ''
    for i in S:
        result += (i*R)
    print(result)