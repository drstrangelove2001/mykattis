from sys import stdin
from collections import deque
from math import inf
from heapq import heappop, heappush
n = int(stdin.readline())
spots = [tuple(map(int, stdin.readline().split())) for _ in range(n + 2)]

class_path_AL = [[(spots[i][0] - spots[j][0])**2 + (spots[i][1] - spots[j][1])**2 if i!=j else 0 for j in range(n+2) ] for i in range(n+2)]

sweat_matrix = [inf]*(n+2)
sweat_matrix[n] = 0
class_path = [(0,n)]

parent_spots = [-1]*(n+2)

final_path = deque()
visited_spots = [False]*(n+2)
while class_path:
    sweat, spot = heappop(class_path)
    if spot == n+1:
        break
    curr_sweat = sweat_matrix[spot]
    if sweat == curr_sweat and not visited_spots[spot]:
        visited_spots[spot] = True
        for next_spot, next_sweat in enumerate(class_path_AL[spot]):
            new_sweat = curr_sweat + next_sweat
            if sweat_matrix[next_spot] <= new_sweat:
                continue
            sweat_matrix[next_spot] = new_sweat
            parent_spots[next_spot] = spot
            heappush(class_path, (new_sweat, next_spot))

while spot != n:
    if 0 <= spot < n:
        final_path.appendleft(spot)
    spot = parent_spots[spot]

if final_path:
    [print(x) for x in final_path]
else:
    print('-')