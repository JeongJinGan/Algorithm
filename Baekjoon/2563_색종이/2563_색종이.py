import sys

sys.stdin = open("2563.txt", "r")

matrix = [[0] * 100 for _ in range(100)]

T = int(input())

for _ in range(T):
    x, y = map(int, input().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            matrix[i][j] = 1
            
print(sum(map(sum, matrix)))


