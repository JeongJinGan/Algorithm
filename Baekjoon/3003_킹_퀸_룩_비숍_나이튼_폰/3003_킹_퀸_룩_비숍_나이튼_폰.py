import sys

sys.stdin = open("3003.txt", "r")

matrix = [1, 1, 2, 2, 2, 8]
list_ = list(map(int, input().split()))
result = [0] * 6
for i in range(6):
    result[i] = matrix[i] - list_[i]

print(*result)