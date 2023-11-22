from sys import stdin
from collections import defaultdict
from math import inf
import heapq
N,S,T = map(int, stdin.readline().split())
adj_list = defaultdict(lambda: list())
distance_matrix = defaultdict(lambda: inf)
for i in range(N):
    dist_array = list(map(int, stdin.readline().split()))
    for j in range(N):
        if i!=j:
            adj_list[i].append((j, dist_array[j]))
distance_matrix[S] = 0
meeting_path = [(0,S)]
while meeting_path:
    dist, park = heapq.heappop(meeting_path)
    if park == T:
        break
    for tmp_dest, tmp_dist in adj_list[park]:
        if distance_matrix[tmp_dest] > distance_matrix[park] + tmp_dist:
            distance_matrix[tmp_dest] = distance_matrix[park] + tmp_dist
            heapq.heappush(meeting_path, (distance_matrix[tmp_dest], tmp_dest))
print(dist)