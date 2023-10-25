import sys
import heapq
N,K = [int(x) for x in sys.stdin.readline().split()]
A = []
occurrences = dict()
for num in sys.stdin.readline().split():
    num = int(num)
    if num in occurrences:
        occurrences[num] -= 1
    else:
        occurrences[num] = -1
A = list(occurrences.values())
heapq.heapify(A)
for _ in range(K):
    x = heapq.heappop(A)
    x += 1
    heapq.heappush(A,x)
print(abs(A[0]))

