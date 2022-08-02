import sys

sys.stdin = open("25192.txt", "r")

N = int(input())

dic_ = {} # 딕셔너리  - 이름 : enter이후 입장횟수
cnt = 0 # 곰곰티콘 횟수
for _ in range(N):
    n = input() # 닉네임 입력

    if n == 'ENTER': # n이 ENTER이라면
        for key, value in dic_.items(): # 딕셔너리 순회
            if value == 1: # value값이 1이라면
                cnt += 1 # cnt증가

        dic_ = {} # 딕셔너리 초기화
        
    
    else: 
        dic_[n] = 1 # 딕셔너리에 이름 : 1 저장

    
for key, value in dic_.items(): # 딕셔너리 순회
    if value == 1: # value값이 1이라면
        cnt += 1 # cnt증가 (for-if 부분에서 cnt증가 + else부분)
print(cnt)