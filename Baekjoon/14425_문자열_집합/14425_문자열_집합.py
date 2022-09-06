import sys

sys.stdin = open("14425.txt", "r")

N, M = map(int, input().split())
list_N = []
list_M = []

for i in range(N):
    list_N.append(input())

for j in range(M):
    list_M.append(input())

cnt = 0

for k in list_M:
    if k in list_N:
        cnt += 1

print(cnt)



