# 시간초과
# N, M = map(int, input().split())
# name_hear_list_ = []
# name_see_list_ = []
# no_hear_see_ = []
# for i in range(N):
#     name = input()
#     name_hear_list_.append(name)
# for i in range(M):
#     name = input()
#     name_see_list_.append(name)

# for j in range(N):
#     for k in range(M):
#         if name_hear_list_[j] in name_see_list_[k]:
#             no_hear_see_.append(name_hear_list_[j])
# no_hear_see_ = sorted(no_hear_see_)
# print(len(no_hear_see_))
# print(*no_hear_see_, sep='\n')

N, M = map(int, input().split())
no_hear = set()
for i in range(N):
    no_hear.add(input())

no_see = set()
for j in range(M):
    no_see.add(input())

no_hear_see = sorted(list(no_hear & no_see))

print(len(no_hear_see))

for k in no_hear_see:
    print(k)