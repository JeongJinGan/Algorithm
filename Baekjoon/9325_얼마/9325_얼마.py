import sys

sys.stdin = open("9325.txt", "r")

T = int(input())

for _ in range(T):
    s = int(input())
    n = int(input())
    car = s

    for i in range(n):
        q, p = map(int, input().split())
        car += q * p

    print(car)
