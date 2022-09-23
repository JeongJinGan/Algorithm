import sys

sys.stdin = open("2440.txt", "r")

N = int(input())

j = 0
for i in range(N,0,-1):
    print('*'*i, end="")
    print(''*j)  
    j += 1