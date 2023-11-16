import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
m,n = map(int, sys.stdin.readline().split())
amoeba_grid = []
for _ in range(m):
    row = sys.stdin.readline()
    amoeba_grid.append(row)
visited = defaultdict(lambda: False)
loops = 0
def amoeba_path(start: tuple):
    i,j = start
    visited[(i,j)] = True
    surrounding_areas = [(i,j-1), (i-1,j-1), (i-1,j), (i-1,j+1), (i,j+1), (i+1,j+1), (i+1,j), (i+1,j-1)]
    for area in surrounding_areas:
        ni, nj = area
        if visited[(ni,nj)]:
            continue
        if 0<=ni<m and 0<=nj<n and amoeba_grid[ni][nj] == '#':
            amoeba_path((ni, nj))

for i in range(m):
    for j in range(n):
        if amoeba_grid[i][j] == '#' and not visited[(i,j)]:
            amoeba_path((i,j))
            loops += 1
print(loops)