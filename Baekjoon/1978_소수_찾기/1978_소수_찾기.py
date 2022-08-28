import sys

sys.stdin = open("1978.txt", "r")

T = int(input())
num = map(int, input().split())
dec = 0
for n in num:
    cnt = 0
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                cnt += 1
        if cnt == 0:
            dec += 1
print(dec)


