from collections import deque

N, M = map(int, input().split())  # 큐의 크기 N, 뽑아내고자 하는 수의 개수 M
idxs = list(map(int, input().split()))  # 뽑아내려고 하는 원소의 위치
dq = deque([i for i in range(1, N + 1)])  # 위치와 원소를 같게 설정

cnt = 0
for i in idxs:
    while True:
        if dq[0] == i:  # [0]이 뽑아내고자 하는 수라면
            dq.popleft()
            break
        else:  # 뽑아내고자 하는 위치가 아니면
            # i의 위치가 중앙보다 앞에 있다면, 앞에서 뒤로
            if dq.index(i) <= len(dq) // 2:
                dq.append((dq.popleft()))
                cnt += 1
            # i의 위치가 중앙보다 뒤에 있다면, 뒤에서 앞으로
            else:
                dq.appendleft((dq.pop()))
                cnt += 1

print(cnt)