X = int(input())
hansu = 0
for i in range(1, X+1):
    X_list = list(map(int, str(i)))
    if i < 100:
        hansu += 1
    elif X_list[0] - X_list[1] == X_list[1] - X_list[2]:
        hansu += 1
print(hansu)        




