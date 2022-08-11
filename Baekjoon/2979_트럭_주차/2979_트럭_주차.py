import sys

sys.stdin = open("2979.txt", "r")


A, B, C = map(int, input().split())
    
matrix = [list(map(int, input().split())) for _ in range(3)]

n = max(matrix[0][1], matrix[1][1], matrix[2][1])
    
board = [0]*(n-1)
    
for truck in matrix:
    for i in range(truck[0] - 1, truck[1] - 1):
        board[i] = board[i] + 1


    
sum_ = 0
for num in board:
    if num == 1:
        sum_ = sum_ + A
    elif num == 2: 
        sum_ = sum_ + 2 * B
    elif num == 3: 
        sum_ = sum_ + 3 * C
print(sum_)