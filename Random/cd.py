# partial output
N,M = map(int, input().split())
ddict = dict()
for _ in range(N):
    x = int(input())
    ddict[x] = 1
count = 0
for _ in range(M):
    x = int(input())
    if x in ddict:
        count += 1
print(count)