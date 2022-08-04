import sys

sys.stdin = open("1547.txt", "r")

ball = [1, 2, 3]
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    N -= 1
    M -= 1
    temp = ball[M]
    ball[M] = ball[N]
    ball[N] = temp

print(ball.index(1)+1)

