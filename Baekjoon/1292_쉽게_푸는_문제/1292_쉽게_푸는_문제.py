# https://www.acmicpc.net/problem/1292
import sys

sys.stdin = open("1292_쉽게_푸는_문제.txt", "r")

A, B = map(int, input().split())
data_ = [0]
sum = 0
for i in range(1, B+1): # 1부터 입력받은 숫자 중 큰 숫자까지
    for j in range(i):  # 2중 for문으로 1일때는 1번 2일때는 2번 3일때는 3번 ...
        data_.append(i) # data_에 넣는다

for i in range(A, B+1): # 입력받은 숫자 사이에 값들을 순회
    sum += data_[i] # sum에 누적
print(sum)



# 코드리뷰(방법만 제안)
# import sys

# # sys.stdin = open("1292_쉽게푸는문제.txt", "r")

# # 수열 = []
# # for i in range(숫자):
# #     수열.append(숫자)
# # 숫자 += 1

# 수열 = []
# A = 3
# B = 7
# N = 1

# # 수열의 얼마만큼 숫자를 추가해야하나?
# # 수열의 길이가 B보다 작을 때까지 수열에 숫자를 추가하자
# while len(수열) < B:

# # N의 크기만큼 수열 리스트에 N을 추가한다
#     for _ in range(N):
#         수열.append(N)
#     N += 1

# print(수열)





# # for문 이용 #
# # N = 1
# # 수열 = []
# # for i in range(B+1):
# #     for _ in range(N):
# #         수열.append(N)
# #         if len(수열) > B:
# #             break
# #     if len(수열) > B:
# #         break
# #     N += 1
# # print(수열)

