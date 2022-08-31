import sys

sys.stdin = open("1427.txt", "r")

N = int(input())

n_ = list(map(int,str(N)))

n_.sort(reverse=True)

for i in n_:
    print(i, end='')