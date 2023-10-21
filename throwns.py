n,k = map(int, input().split())
undo = False
curr = 0
stk = [0]
for move in input().split():
    if not undo and move != 'undo':
        x = int(move)
        if x>=0:
            curr += abs(x)%n
        else:
            curr -= abs(x)%n
        curr = curr%n
        stk.append(curr)
    elif not undo:
        undo = not undo
    elif undo:
        y = int(move)
        for _ in range(y):
            stk.pop()
        curr = stk[-1]
        undo = not undo
print(curr)
