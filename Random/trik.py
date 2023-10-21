moves = input()
ball = 1
d = {'A': {1:2, 2:1, 3:3}, 'B': {1:1, 2:3, 3:2}, 'C': {1:3, 2:2, 3:1}}
for move in moves:
    ball = d[move][ball]
print(ball)