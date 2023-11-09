import sys
from itertools import combinations
n,m = map(int, sys.stdin.readline().split())
if m < n-1 or m > (n*(n-1))//2:
    print(-1)
else:
    sums = set()
    ans = []
    lst = [i for i in range(1,n+1)]
    combs = [(x, y) for x, y in combinations(lst, 2)]
    count = 0
    for x,y in combs:
        if count == m:
            break
        if x+y not in sums:
            ans.append((x,y))
            sums.add(x+y)
            count += 1
    if len(ans) != m:
        print(-1)
    else:
        [print(x,y) for x,y in ans]


