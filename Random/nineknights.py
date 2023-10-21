board = []
attacked = set()
ans = 'v'
count = 0
for i in range(5):
    board.append(input())
for i in range(5):
    for j in range(5):
        if board[i][j] == 'k':
            count += 1
            if (i,j) in attacked:
                ans = 'i'
                break
            else:
                if all((0<(i-1),(j-2)<5)):
                    attacked.add((i-1,j-2))
                if all((0<(i-2),(j-1)<5)):
                    attacked.add((i-2,j-1))
                if all((0<(i-2),(j+1)<5)):
                    attacked.add((i-2,j+1))
                if all((0<(i-1),(j+1)<5)):
                    attacked.add((i-1,j+1))
                if all((0<(i+1),(j-2)<5)):
                    attacked.add((i+1,j-2))
                if all((0<(i+2),(j-1)<5)):
                    attacked.add((i+2,j-1))
                if all((0<(i+2),(j+1)<5)):
                    attacked.add((i+2,j+1))
                if all((0<(i+1),(j+2)<5)):
                    attacked.add((i+1,j+2))
print('valid' if ans=='v' and count == 9 else 'invalid')