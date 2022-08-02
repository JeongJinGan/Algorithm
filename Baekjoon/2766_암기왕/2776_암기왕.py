import sys

sys.stdin = open("2776.txt", "r")

T = int(input())

for _ in range(T):
    N = int(input())
    n = set(map(int, input().split()))
    M = int(input())
    m = list(map(int, input().split()))

    for i in m:
        if i in n:
            print(1)
        else:
            print(0)