import sys

sys.stdin = open("1598.txt", "r")

num1, num2 = map(int, input().split())

# num1의 행, 열
if num1 % 4 == 0:
    row1 = 4
    col1 = num1 // 4
else:
    row1 = num1 % 4
    col1 = num1 // 4
    col1 += 1 


# num2의 행, 열
if num2 % 4 == 0:
    row2 = 4
    col2 = num2 // 4
else:
    row2 = num2 % 4
    col2 = num2 // 4   
    col2 += 1 

    



# print(row1, col1)
# print(row2, col2)
print((abs(row2 - row1) + abs(col2 - col1)))
