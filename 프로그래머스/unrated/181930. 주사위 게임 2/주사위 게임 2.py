def solution(a, b, c):
    answer = 0
    if a != b and b!= c and a != c:
        answer = a+b+c
    elif (a == b and b != c and a != c) or (a != b and b == c and a != c) or (a == c and b != c and a != b):
        answer = (a+b+c)*(a*a+b*b+c*c)
    else:
        answer = (a+b+c)*(a*a+b*b+c*c)*(a*a*a+b*b*b+c*c*c)
    return answer