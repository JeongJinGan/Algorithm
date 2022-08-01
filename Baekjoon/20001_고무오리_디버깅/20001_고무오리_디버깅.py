import sys

sys.stdin = open("20001_고무오리_디버깅.txt", "r")

duck = input() # 고무오리 디버깅 시작
stack = []  # 스택 활용할 리스트
while duck != '고무오리 디버깅 끝': # 고무오리 디버깅 끝이라는 입력이 없다면 계속~
    duck = input()
    if duck == '문제': # 문제가 입력 되었다면
        stack.append(duck) # stack에 추가
    elif duck == '고무오리': # 고무오리가 입력 되었다면
        if stack:
            stack.pop() # stack 문제가 있다면 pop
        else:
            stack.append('문제') # 문제가 없다면 문제 2개 추가
            stack.append('문제')
    

if stack:
    print('힝구') # 한개라도 문제가 남아 있다면 힝구 출력
else:
    print('고무오리야 사랑해') # 없다면 고무오리야 사랑해 출력