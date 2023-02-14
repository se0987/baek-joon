n = int(input())  # 컴퓨터의 개수
e = int(input())  # 연결선의 개수
adj = [[] for i in range(n + 1)]  # 그래프 초기화 (컴퓨터의 개수+1 만큼 빈 리스트)
visited = [0] * (n + 1)  # 방문 체크할 배열

for i in range(e):  # 그래프 생성
    src, dest = map(int, input().split())
    adj[src].append(dest)  # src -> dest 연결
    adj[dest].append(src)  # dest -> src 연결 (양방향)


def dfs(n=1):
    visited[n] = 1 # 방문 체크
    for nx in adj[n]:
        if visited[nx] == 0: # 방문하지 않았다면
            dfs(nx) # 재귀


dfs()
print(sum(visited) - 1)
