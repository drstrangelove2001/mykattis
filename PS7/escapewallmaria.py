import sys
import heapq
t,N,M = map(int, sys.stdin.readline().split())
maria = []
for i in range(N):
    row = sys.stdin.readline()
    maria.append(row)
    if 'S' in row:
        start = (i, row.index('S'))

escape_route = [(0, start)]
visited = set()
escape_regions = [(x,y) for x in range(N) for y in range(M) if x==0 or x==N-1 or y==0 or y==M-1]

def escape_plan(escape_route):
    while escape_route:
        time, curr = heapq.heappop(escape_route)
        if curr in escape_regions:
            return time,curr
        if time >= t:
            return
        if curr in visited:
            continue
        visited.add(curr)
        x,y = curr
        surrounding_areas = [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]
        for area in surrounding_areas:
            nx, ny = area
            if 0<=nx<N and 0<=ny<M:
                if maria[nx][ny] == '0' or (nx == x-1 and maria[nx][ny] == 'D') or (nx == x+1 and maria[nx][ny] == 'U') or (ny == y-1 and maria[nx][ny] == 'R') or (ny == y+1 and maria[nx][ny] == 'L'):
                    area_time = time + 1
                    heapq.heappush(escape_route, (area_time, area))
    return
escape = escape_plan(escape_route)
print(escape[0] if escape else 'NOT POSSIBLE')