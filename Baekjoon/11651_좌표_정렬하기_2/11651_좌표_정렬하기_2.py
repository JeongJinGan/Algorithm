import sys

sys.stdin = open("11651.txt", "r")


N = int(input())
matrix = []

for i in range(N):
    x, y = map(int, input().split())
    matrix.append((x,y))
matrix.sort(key=lambda x : (x[1], x[0]))

for i in range(N):
    print(matrix[i][0],matrix[i][1])

