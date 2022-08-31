import sys

sys.stdin = open("25305.txt", "r")

N, k = map(int, input().split())
list_ = list(map(int, input().split()))

list_.sort()
print(list_[-k])




