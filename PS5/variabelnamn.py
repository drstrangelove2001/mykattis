import sys
from collections import defaultdict
N = int(sys.stdin.readline())
history = set()
variables = defaultdict(lambda:1)
for _ in range(N):
    x = int(sys.stdin.readline())
    if x not in history:
        variables[x] = 2
    else:
        tmp = x*variables[x]
        while tmp  in history:
            variables[x] += 1
            tmp = x*variables[x]
        x = tmp
    print(x)
    history.add(x)
