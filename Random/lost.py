#Incorrect - dont refer!

from sys import stdin
from collections import defaultdict
from math import inf, isinf
import heapq
n,m = map(int, stdin.readline().split())
langs = ['English'] + stdin.readline().split()
lang_AL = defaultdict(list)
cost_matrix = defaultdict(lambda: inf)
cost_matrix['English'] = 0
translated = defaultdict(lambda: False)
lang_queue = []
for _ in range(m):
    a,b,c = stdin.readline().split()
    if not translated[b]:
        lang_AL[a].append((b,int(c)))
    if a == 'English':
        cost_matrix[b] = 0
        translated[b] = True
        heapq.heappush(lang_queue, (0, b))
while lang_queue:
    cost, lang = heapq.heappop(lang_queue)
    if cost > cost_matrix[lang]:
        continue
    for translated_lang, cost_of_translation in lang_AL[lang]:
        if cost_matrix[translated_lang] > cost_matrix[lang] + cost_of_translation:
            cost_matrix[translated_lang] = cost_matrix[lang] + cost_of_translation
            heapq.heappush(lang_queue, (cost_matrix[translated_lang], translated_lang))
total_cost = 0
for lang, costt in lang_AL['English']:
    total_cost += costt
impossible = False
for i in range(1,n+1):
    if isinf(cost_matrix[langs[i]]):
        impossible = True
        break
    total_cost += cost_matrix[langs[i]]
print(total_cost if not impossible else 'Impossible')