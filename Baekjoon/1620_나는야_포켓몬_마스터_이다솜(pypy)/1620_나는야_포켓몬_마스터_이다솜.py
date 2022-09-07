import sys

sys.stdin = open("1620.txt", "r")

# N, M = map(int, input().split())

# pok_ = [0]
# for i in range(1, N+1):
#     pok_.append(input())

# find_ = []
# for j in range(M):
#     find_.append(input())

# a_find = []
# for k in find_:
#     if k > '0' and k <'999':
#         k = int(k)
#         a_find.append(k)
#     else:
#         a_find.append(k)

# print(a_find[0])
# for q in range(M):
#     if a_find[q] > 0:
#         print(pok_[a_find[q]])    
#     else:
#         print(pok_.index(a_find[q]))
        
# N, M = map(int, sys.stdin.readline().split())
# pok_num = {}
# pok_name = {}

# for i in range(1, N+1):
#     pok = input()
#     pok_num[i] = pok
#     pok_name[pok] = i

# for _ in range(M):
#     x = input()
#     if x.isdigit():
#         print(pok_num[int(x)])
#     else:
#         print(pok_name[x])

n, m = map(int, input().split())

dict = {}

for i in range(1, n + 1):
    a = input().rstrip()
    dict[i] = a
    dict[a] = i

for i in range(m):
    quest = input().rstrip()
    if quest.isdigit():
        print(dict[int(quest)])
    else:
        print(dict[quest])