import sys

sys.stdin = open("5576.txt", "r")

list_ = []
for _ in range(20):
    univ_ = int(input())
    list_.append(univ_)

W_ = []
K_ = []

for i in range(10):
    W_.append(list_[i])

for j in range(10, 20):
    K_.append(list_[j])

W_.sort(reverse= True)
K_.sort(reverse= True)
W_sum = 0
K_sum = 0

for k in range(3):
    W_sum += W_[k]
    K_sum += K_[k]

print(W_sum, K_sum)



