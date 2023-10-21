inp = input().split()
H = int(inp[0])
seq = inp[1] if len(inp) > 1 else ''
r = 2**(H+1)-1
ind = 1
for move in seq:
    if move == 'L':
        ind *= 2
    elif move == 'R':
        ind = 2*ind + 1
print(r-ind+1)
