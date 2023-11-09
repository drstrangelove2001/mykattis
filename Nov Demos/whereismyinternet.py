import sys
from collections import defaultdict
N,M = map(int, sys.stdin.readline().split())
sys.setrecursionlimit(10**6)
houses = defaultdict(lambda: list())
for _ in range(M):
    a,b = map(int, sys.stdin.readline().split())
    houses[a].append(b)
    houses[b].append(a)
visited = [False]*(N+1)
def dfs(x):
    visited[x] = True
    for h in houses[x]:
        if visited[h]:
            continue
        dfs(h)
dfs(1)
if all(visited[1:]):
    print('Connected')
else:
    [print(ind) for ind, x in enumerate(visited) if not x and ind>0]