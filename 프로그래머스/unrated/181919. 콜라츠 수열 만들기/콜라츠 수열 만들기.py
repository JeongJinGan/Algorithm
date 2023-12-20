def solution(n):
    answer = []
    num = n
    answer.append(n)
    while 1:
        if num % 2 == 0:
            num = num // 2
            answer.append(num)
        else:
            num = 3 * num + 1
            answer.append(num)
        if num == 1:
            break
    return answer
        
solution(10)