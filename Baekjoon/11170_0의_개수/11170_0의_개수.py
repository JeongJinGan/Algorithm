import sys

sys.stdin = open("11170.txt", "r")

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    cnt = 0
    for i in range(N, M+1):
        change = str(i)
        cnt += change.count('0')
    
    print(cnt)

