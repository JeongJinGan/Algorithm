import sys

sys.stdin = open("2693.txt", "r")

T = int(input())

for _ in range(T):
    list_ = list(map(int, input().split()))
    list_.sort()
    print(list_[-3])