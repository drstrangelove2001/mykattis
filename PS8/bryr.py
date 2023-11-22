from sys import stdin
from collections import defaultdict
import heapq
n,m = map(int, stdin.readline().split())
bridge_map = defaultdict(lambda: list())
route = [(0,1)]
for _ in range(m):
    a,b,c = map(int, stdin.readline().split())
    bridge_map[a].append((b,c))
    bridge_map[b].append((a,c))
lanes_dict = defaultdict(lambda: 10**6)
lanes_dict[1] = 0
single_lanes_to_cross = 0
while route:
    lanes_crossed, area = heapq.heappop(route)
    if area == n:
        single_lanes_to_cross = lanes_crossed
        break
    for dest, lane in bridge_map[area]:
        if lanes_dict[dest] > lanes_dict[area] + lane:
            lanes_dict[dest] = lanes_dict[area] + lane
            heapq.heappush(route, (lanes_dict[dest], dest))
print(single_lanes_to_cross)