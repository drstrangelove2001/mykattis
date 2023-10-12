scores = {'A':(11,11), 'K':(4,4), 'Q':(3,3), 'J': (20,2), 'T':(10,10), '9':(14,0), '8':(0,0), '7':(0,0)}
N,B = input().split()
N = int(N)
A = [input() for _ in range(4*N)]
score = 0
for hand in A:
    if hand[1] == B:
        score += scores[hand[0]][0]
    else:
        score += scores[hand[0]][1]
print(score)