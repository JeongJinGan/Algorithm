N, A = map(int, input().split())
X = list(map(int, input().split())) # 정수 N개 입력받기
for i in range(0, N):
    if X[i] < A:    # 리스트로 입력받은 값에서 A보다 작으면
        print(X[i], end=' ')    # 출력
