import sys
from collections import defaultdict
import heapq
N,M = map(int, sys.stdin.readline().split())
island_AL = defaultdict(lambda: list())

for _ in range(M):
    u,v = map(int, sys.stdin.readline().split())
    island_AL[u].append(v)
    island_AL[v].append(u)
q = []
army_strength = dict()
for i in range(1,N+1):
    s = int(sys.stdin.readline())
    army_strength[i] = s

visited = [False]*(N+1)
visited[1] = True
strength = army_strength[1]
heapq.heappush(q, (strength, 1))

while len(q)>0:
    u = heapq.heappop(q)
    if u[1] != 1:
        if u[0] >= strength:
            break
        strength += u[0]
    for near_island in island_AL[u[1]]:
        if not visited[near_island]:
            heapq.heappush(q, (army_strength[near_island], near_island))
            visited[near_island] = True
print(strength)