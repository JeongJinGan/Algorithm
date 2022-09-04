import sys
import operator

sys.stdin = open("10814.txt", "r")

T = int(input())
# dic_ = {}
# for i in range(T):
#     age, name = map(str, input().split())
#     dic_[name] = age
# print(dic_)
# # dic_ = sorted(dic_.items(), key=lambda x:x[1])
# dic_ = sorted(dic_.items(), key = lambda x: (len(x[1]), x[1]))
# for key, value in dic_:
#     print(value, key)

matrix = [list(map(str, input().split())) for _ in range(T)]
matirx_ = matrix.sort(key=lambda x:x[0])
for key, value in matrix:
    print(int(key), value)

