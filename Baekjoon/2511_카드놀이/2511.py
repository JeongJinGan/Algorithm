A = list(map(int, input().split()))
B = list(map(int, input().split()))
A_score = 0
B_score = 0
if A == B:
    print(10, 10)
    print('D')
else:
    for i in range(0, 10):
        if A[i] > B[i]:
            A_score += 3
            win = 'A'
        elif A[i] < B[i]:
            B_score += 3
            win = 'B'
        else:
            A_score += 1
            B_score += 1

    print(A_score, B_score)
    if A_score == B_score:
        print(win)
    elif A_score < B_score:
        print('B')
    else:
        print('A')
        