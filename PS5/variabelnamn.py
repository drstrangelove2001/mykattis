from collections import defaultdict
N = int(input())
history = set()
variables = defaultdict(lambda:1)
for _ in range(N):
    x = int(input())
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
