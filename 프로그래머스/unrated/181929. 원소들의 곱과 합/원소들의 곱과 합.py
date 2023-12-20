def solution(num_list):
    answer = 0
    num1 = 0
    num2 = 1
    for i in range(len(num_list)):
        num1 += num_list[i]
        num2 *= num_list[i]
    
    num1 = num1 * num1
    
    if num2 < num1:
        answer = 1
    else:
        answer = 0
        
    return answer