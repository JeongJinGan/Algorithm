import sys

sys.stdin = open("10816.txt", "r")

N = int(input()) # 첫번째로 받을 수
N_list = list(map(int, input().split())) # int형으로 받아서 리스트에 넣기
M = int(input()) # 두번째로 받을 수
M_list = list(map(int, input().split())) # int형으로 받아서 리스트에 넣기

dic_ = dict()

for num in N_list: # 첫번째로 숫자들을 받은 리스트 순회
    if num in dic_: # 리스트들이 딕셔너리 안에 있으면 
        dic_[num] += 1 # 누적 + 1
    else: # 딕셔너리 안에 없으면
        dic_[num] = 1 # 새롭게 + 1  

for num in M_list: # 두번째로 숫자들을 받은 리스트 순회
    if num in dic_: # 리스트들이 딕셔너리 안에 있으면
        print(dic_[num], end = " ") # 해당하는 숫자의 값(values)을 출력
    else: # 없으면
        print(0, end = " ") # 0을 출력


# 딕셔너리 수업이라 딕셔너리 이용해서 풀으라고 하시는 것 같아서 딕셔너리 이용했습니다.
# 백준 예시 처럼 
# 10 - N
# 6 3 2 10 10 10 -10 -10 7 3 - N_list
# 8 - M
# 10 9 -5 2 3 4 5 -10 - M_list
# 이렇게 값을 받는다고 하면 
# N_list의 값들이 M_list의 각각의 숫자들이 몇개씩있냐가 문제니까
# N_list들을 딕셔너리에 넣었습니다. (숫자와, 몇번 등장했는지)
# => {6: 1, 3: 2, 2: 1, 10: 3, -10: 2, 7: 1} 이렇게 저장
# 이제 M_list들을 순회하면서 각각의 값들이 딕셔너리에 있나 확인
# 있으면 dic_[해당숫자] 값 출력, 없으면 0 출력 

