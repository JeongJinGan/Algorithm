import sys

sys.stdin = open("14467.txt", "r")

N = int(input())
cows = [-1] * 11
cnt = 0
for _ in range(N):
    cow, road = map(int, input().split())

    if cows[cow] == -1:
        cows[cow] = road
    else:
        if cows[cow] != road:
            cnt += 1
            cows[cow] = road

print(cnt)




