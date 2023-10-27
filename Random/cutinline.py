N = int(input())
A = [input() for _ in range(N)]
C = int(input())
for _ in range(C):
    event = input().split()
    if event[0] == 'cut':
        ind = A.index(event[2])
        A.insert(ind, event[1])
    else:
        A.remove(event[1])
[print(x) for x in A]