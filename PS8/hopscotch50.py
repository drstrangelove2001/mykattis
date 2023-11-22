from sys import stdin
from collections import defaultdict
import heapq
n,k = map(int, stdin.readline().split())
art_matrix = defaultdict(lambda: list())
hops = []
distance_matrix = defaultdict(lambda: 10**6)
for i in range(n):
    row = list(map(int, stdin.readline().split()))
    for j in range(n):
        val = row[j]
        art_matrix[val].append((i,j))
        if val == 1:
            heapq.heappush(hops, (0, val, i, j))
            distance_matrix[(i,j)] = 0
hopped_to_k = -1
while hops:
    d,val,i,j = heapq.heappop(hops)
    if val == k:
        hopped_to_k = d
        break
    for ni, nj in art_matrix[val+1]:
        dist = abs(ni - i) + abs(nj - j)
        if distance_matrix[(ni,nj)] > distance_matrix[(i,j)] + dist:
            distance_matrix[(ni,nj)] = distance_matrix[(i,j)] + dist
            heapq.heappush(hops, (distance_matrix[(ni,nj)], val+1, ni, nj))
print(hopped_to_k)
