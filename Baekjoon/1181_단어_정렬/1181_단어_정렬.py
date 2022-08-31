import sys

sys.stdin = open("1181.txt", "r")

N = int(input())
matrix = []
for i in range(N):
    words = input()
    matrix.append(words)

set_ = list(set(matrix))
set_.sort()
set_.sort(key=len)


for i in set_:
    print(i)
