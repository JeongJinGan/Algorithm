import sys

sys.stdin = open("2442.txt", "r")

N = int(input())

j = 0

for i in range(2*N-1,0,-2):
    print(" "*j, end="")
    print('*'*i)
    j += 1