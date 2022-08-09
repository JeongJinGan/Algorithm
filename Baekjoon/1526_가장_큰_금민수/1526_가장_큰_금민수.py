import sys

sys.stdin = open("1526.txt", "r")

N = int(input()) # 입력받기

while True: # 무한반복
    # 입력받은 글자의 길이가 '4' 혹은 '7'의 개수와 같다면
    if len(str(N)) == str(N).count('4') + str(N).count('7'):
        # N을 출력
        print(N)
        break
    # 같지 않다면 N을 -1씩 해준다    
    N  -= 1


