T = 4
for tc in range(T):
    nx, ny, np, nq, mx, my, mp, mq = map(int, input().split())
    # 겹치는 부분 -> 면/선/점/X : 4가지
    # 겹치는 부분이 면/선/점/X 인지 판별해서 해당 코드 문자 출력 (a/b/c/d)

    # n = [[x, y]for x in range(nx, mx) for y in range(ny, my)]
    nbox_x = set(list(range(nx, np+1)))
    mbox_x = set(list(range(mx, mp+1)))
    nmx = nbox_x.intersection(mbox_x)

    nbox_y = set(list(range(ny, nq+1)))
    mbox_y = set(list(range(my, mq+1)))
    nmy = nbox_y.intersection(mbox_y)

    if len(nmx) == 0 or len(nmy) == 0: # 둘 중 하나라도 겹치는게 없다면
        print('d') #공통부분 없음

    elif len(nmx) >= 2:
        if len(nmy) >= 2:
            print('a')
        else:
            print('b')
            
    else:
        if len(nmy) >= 2:
            print('b')
        else:
            print('c')