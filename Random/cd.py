import sys
from collections import defaultdict
while True:
    N,M = map(int, sys.stdin.readline().split())
    if N==0 and M==0:
        break
    cds = defaultdict(lambda : 0)
    count = 0
    for _ in range(N):
        x = int(sys.stdin.readline())
        cds[x] = 1
    for _ in range(M):
        y = int(sys.stdin.readline())
        if cds[y]:
            count += 1
    print(count)