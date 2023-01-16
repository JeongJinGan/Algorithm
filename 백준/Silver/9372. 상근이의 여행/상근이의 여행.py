import sys
# 테스트케이스 수
T = int(sys.stdin.readline())

for t in range(T):

    # 국가의 수, 비행기의 종류
    N, M = list(map(int, sys.stdin.readline().split()))

    # 인접영행렬(그래프의 간선이 하나도 없는 빈 이차원 행렬)
    matrix = [[0]*(N+1) for i in range(N+1)]

    # 입력받는 값에 대해 영형렬에 1삽입(인접리스트생성)
    for i in range(M):
        a, b = map(int,sys.stdin.readline().split())
        matrix[a].append(b)
        matrix[b].append(a)
        # matrix[a][b]=matrix[b][a]=1

    # 방문한곳 체크기록할 리스트
    visited_dfs = [0]*(N+1)

    def dfs(V, cnt):
        visited_dfs[V]=1
        #재귀
        for i in matrix[V]:
            if visited_dfs[i] == 0:
                cnt = dfs(i, cnt + 1)
        return cnt

    res = dfs(1,0)
    print(res-1)
