from sys import stdin
from collections import defaultdict
from math import inf, isfinite
import heapq
while True:
    n,m,q,s = map(int, stdin.readline().split())
    if n == m == q == s == 0:
        break
    adj_list = defaultdict(lambda: list())
    for _ in range(m):
        u,v,w = map(int, stdin.readline().split())
        adj_list[u].append((v,w))
    pr_queue = [(0,s)]
    dist_matrix = defaultdict(lambda: inf)
    dist_matrix[s] = 0
    while pr_queue:
        dist, node = heapq.heappop(pr_queue)
        for tmp_dest, tmp_dist in adj_list[node]:
            if dist_matrix[tmp_dest] > dist_matrix[node] + tmp_dist:
                dist_matrix[tmp_dest] = dist_matrix[node] + tmp_dist
                heapq.heappush(pr_queue, (dist_matrix[tmp_dest], tmp_dest))
    for _ in range(q):
        dest = int(stdin.readline())
        print(dist_matrix[dest] if isfinite(dist_matrix[dest]) else 'Impossible')
    print()