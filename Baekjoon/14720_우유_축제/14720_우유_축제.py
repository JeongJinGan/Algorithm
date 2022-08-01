import sys

sys.stdin = open("14720_우유_축제.txt", "r")

N = int(input())
n = list(map(int, input().split()))

cnt = 0

for i in range(N):
    if n[i] == cnt % 3:
        cnt += 1

print(cnt)