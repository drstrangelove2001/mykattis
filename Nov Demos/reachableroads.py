import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())

for _ in range(n):
    m = int(sys.stdin.readline())
    r = int(sys.stdin.readline())
    roadlines = defaultdict(lambda: list())
    for _ in range(r):
        u,v = map(int, sys.stdin.readline().split())
        roadlines[u].append(v)
        roadlines[v].append(u)
    visited = [False]*(m)
    counter = -1
    def dfs(x):
        visited[x] = True
        for r in roadlines[x]:
            if visited[r]:
                continue
            dfs(r)
    while not all(visited):
        dfs(visited.index(False))
        counter += 1
    print(counter)