T = int(input())

for _ in range(T):
    # 그 다음 줄부터 각각의 테스트 케이스에 대해 정수 a와 b가 주어진다.
    a, b = map(int, input().split())
    a = a % 10  # 17의 n승과 7의 n승의 1의 자리수는 같음
    
    # 제곱 시 1의 자리 수를 구하고 반복에 따라 구분, 따로 구해서 나누기
    if a == 0:
        print(10)

    elif a == 1 or a == 5 or a == 6:    # 그대로 유지
        print(a)

    elif a == 4 or a == 9:  # 2개 반복
        b = b%2
        if b == 1:
            print(a)
        else:
            print((a*a)%10)

    else:   # 4개 반복
        b = b%4 
        if b == 0:
            print((a**4)%10)
        else:
            print((a**b)%10)