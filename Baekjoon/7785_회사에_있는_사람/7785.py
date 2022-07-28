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