import sys

sys.stdin = open("1453.txt", "r")

N = int(input())

num = list(map(int, input().split()))

result = len(set(num))
print(N - result)




