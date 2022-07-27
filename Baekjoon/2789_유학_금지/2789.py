cambridge = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']
word = input()

for i in cambridge:
     word = word.replace(i,'')

print(word)

# 리스트(.remove) 이용
# word = list(input())
# for i in word:
#     if i in 'CAMBRIDGE':
#         word.remove(i)

# for i in word:
#     print(i, end = "")