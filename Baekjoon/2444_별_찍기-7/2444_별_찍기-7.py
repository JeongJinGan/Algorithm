import sys

sys.stdin = open("2442.txt", "r")

N = int(input())

j = N-1

for i in range(1,2*N,2):
    print(" "*j, end="")
    print('*'*i)
    j -= 1

j = 1
for i in range(2*N-3,0,-2):
    print(" "*j, end="")
    print('*'*i)
    j += 1