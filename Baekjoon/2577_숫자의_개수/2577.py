num1, num2, num3 = map(int, input().split())
num = str(num1 * num2 * num3) # 입력된 3개의 곱한 값을 문자열로변환 후 변수에 넣기
result = [0]*10 # 배열안의 값을 0으로 10개 초기화

for i in num:
    result[int(i)] += 1 # num을 각각 쪼개서 해당하는 인덱스에 +1씩 해주기

for i in result:
    print(i)