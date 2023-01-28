M1 = int(input())
N1 = set(map(int, input().split())) 
M2 = int(input())
N2 = list(map(int, input().split())) 

for num in N2:
    if num in N1:
        print(1)
    else:
        print(0)