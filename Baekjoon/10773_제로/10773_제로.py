import sys

sys.stdin = open("10773_제로.txt", "r")
K = int(input())

input_list = []

for _ in range(K):
    input_list.append(int(input()))

    stack = []

    for elem in input_list:
        if elem != 0:
            stack.append(elem)
        else:
            stack.pop()
print(sum(stack))
    

# 간단하게
# stack = []
# for _ in range(int(input())):
#     number = int(input())

#     if number == 0:
#         stack.pop()
#     else:
#         stack.append(number)
# print(sum(stack))