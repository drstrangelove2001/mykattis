T = int(input())
for i in range(T):
    count=0
    P,R,F = map(int,input().split())
    while P<=F:
        P *= R
        count += 1
    print(count)