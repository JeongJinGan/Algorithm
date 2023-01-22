T = int(input())
list_ = []
sung = []
player = []
player_sung = []
for i in range(T):
    name = input()
    list_.append(name)

for j in range(len(list_)):
    sung.append((list_[j][0]))
    if sung.count(list_[j][0]) >= 5:
        player.append(sung[j][0])
if len(player) == 0:
    print('PREDAJA')  
else:
    player.sort()
    for play in player:
        if play not in player_sung:
            player_sung.append(play)
for k in range(len(player_sung)):
    print(player_sung[k], end="")