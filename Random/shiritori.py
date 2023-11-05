import sys
from collections import defaultdict
N = int(sys.stdin.readline())
player = 1
played_words = defaultdict(lambda:False)
prev_word = ''
fair = True
for _ in range(N):
    word = sys.stdin.readline().strip()
    if played_words[word]:
        print(f'Player {player} lost')
        fair = False
        break
    else:
        if prev_word and word[0] != prev_word[-1]:
            print(f'Player {player} lost')
            fair = False
            break
        else:
            played_words[word] = True
            prev_word = word
    player = 2 if player == 1 else 1
if fair:
    print('Fair Game')
