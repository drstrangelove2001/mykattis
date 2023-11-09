import sys
N,M = map(int, sys.stdin.readline().split())
waterflow_grid = []
for i in range(N):
    gridrow = list(sys.stdin.readline().strip())
    waterflow_grid.append(gridrow)
flow = True
while flow:
    flow = False
    for i in range(N):
        for j in range(M):
            if i < N-1 and waterflow_grid[i][j] == 'V':
                if waterflow_grid[i+1][j] == '.':
                    waterflow_grid[i+1][j] = 'V'
                    flow = True
                elif waterflow_grid[i+1][j] == '#':
                    if j > 0 and waterflow_grid[i][j-1] == '.':
                        waterflow_grid[i][j-1] = 'V'
                        flow = True
                    if j < M-1 and waterflow_grid[i][j+1] == '.':
                        waterflow_grid[i][j+1] = 'V'
                        flow = True
for row in waterflow_grid:
    print(''.join(row))
