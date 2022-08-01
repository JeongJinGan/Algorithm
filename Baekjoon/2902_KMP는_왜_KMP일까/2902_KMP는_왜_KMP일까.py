import sys

sys.stdin = open("2902_KMP는_왜_KMP일까.txt", "r")

kmp = input().split('-')
for i in range(len(kmp)):
    print(kmp[i][0], end='')

