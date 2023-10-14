N = int(input())
players = [input() for _ in range(N)]
flag=0
for ind in range(N-1):
    if players[ind] < players[ind+1]:
        if flag == -1:
            flag = 0
            break
        flag = 1
    elif players[ind] > players[ind+1]:
        if flag == 1:
            flag = 0
            break
        flag = -1
print('INCREASING' if flag == 1 else ('DECREASING' if flag == -1 else 'NEITHER'))