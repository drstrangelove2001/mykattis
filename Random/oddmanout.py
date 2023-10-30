N = int(input())
for i in range(1,N+1):
    G = int(input())
    A = list(map(int, input().split()))
    ddict = dict()
    for C in A:
        if C in ddict:
            del ddict[C]
        else:
            ddict[C] = 1
    print(f'Case #{i}: {next(iter(ddict))}')