import sys

sys.stdin = open("7785.txt", "r")
n = int(input()) # 몇명의 데이터를 입력 받을 것인가
dic_ = dict()   # key value 형태로 되어 있어서 딕셔너리 생성
for i in range(n):
    name, record = input().split() # 이름과 , 출퇴근 입력
    if record == 'enter': # 입력받은 값이 출근(enter)이라면
        dic_[name] = 1 # 딕셔너리에 해당하는 이름 = 1
    else: 
        # dic_.pop(name) # (출력결과가 시간초과)
        del dic_[name]  # 출근이 아니라면(퇴근) del 지워준다

dic_ = sorted(dic_.keys(), reverse=True) # 역순으로(이름만)
for j in dic_:
    print(j)



# 코드리뷰
# N = int(input())
# logs = dict()
# for i in range(N):
#     key, value  = input().split()
#     logs[key] = value 

# # print(logs)

# # logs["baha"] = 'enter'
# # logs["askr"] = 'enter'
# # logs["baha"] = 'leave'
# # logs["artem"] = 'enter'

# # print(logs)

# list_ = []
# for key in logs:
#     # print(key)
#     # value가 enter인 key를 찾아서 리스트에 저장
#     if logs[key] == 'enter':
#         list_.append(key)

# # print(list_)
# list_.sort(reverse=True)
# # print(list_)
# for name in list_:
#     print(name)

