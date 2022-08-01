import sys

sys.stdin = open("1076_저항.txt", "r")

color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

color1 = input()
color2 = input()
color3 = input()
result = str(color.index(color1)) + str(color.index(color2))
print(int(result) * (10 ** color.index(color3)))