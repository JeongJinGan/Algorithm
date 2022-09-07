import sys

sys.stdin = open("11478.txt", "r")

word = input()
result = []
for i in range(len(word)):
    for j in range(i, len(word)):
        aw = word[i:j+1]
        result.append(aw)

print(len(set(result)))
