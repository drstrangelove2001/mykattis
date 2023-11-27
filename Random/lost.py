from sys import stdin
from collections import defaultdict, deque
from math import inf, isinf

n,m = map(int, stdin.readline().split())
langs = stdin.readline().split()
lang_AL = defaultdict(list)

for _ in range(m):
    a,b,c = stdin.readline().split()
    lang_AL[a].append((b,int(c)))
    lang_AL[b].append((a,int(c)))

lang_queue = deque(['English'])

cost_matrix = defaultdict(lambda: inf)
level = defaultdict(lambda: inf)

cost_matrix['English'] = level['English'] = 0

while lang_queue:
    lang = lang_queue.popleft()
    for tlang, tcost in lang_AL[lang]:
        if isinf(level[tlang]):
            level[tlang] = level[lang] + 1
            cost_matrix[tlang] = tcost
            lang_queue.append(tlang)
        if level[tlang] == level[lang] + 1:
            cost_matrix[tlang] = min(cost_matrix[tlang], tcost)

imp = False
total_cost = 0
for lang in langs:
    if isinf(level[lang]):
        imp = True
        break
    else:
        total_cost += cost_matrix[lang]
print(total_cost if not imp else 'Impossible')