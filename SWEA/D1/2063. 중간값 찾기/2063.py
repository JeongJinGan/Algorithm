import sys

sys.stdin = open("2063_input.txt", "r")

T = int(input())
a = list(map(int, input().split()))
a.sort()    # 정렬
print(a[int((T-1)/2)]) # 인덱스는 0번부터여서 T-1값(마지막) 의 절반 출력