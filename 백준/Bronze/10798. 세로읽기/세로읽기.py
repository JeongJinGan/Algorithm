list_ = []
len_ = []
T = 5
for i in range(T):
    word = input()
    list_.append(word)
    len_.append(len(word))

words = ''

for j in range(max(len_)):
    for k in range(T):
        if j < len_[k]:
            words += list_[k][j]

print(words)