T = 3
for i in range(T):
    x = list(map(int, input().split()))
    yout = sum(x)
    if yout == 0:
        print("D")
    elif yout == 1:
        print("C")
    elif yout == 2:
        print("B")
    elif yout == 3:
        print("A")
    elif yout == 4:
        print("E")