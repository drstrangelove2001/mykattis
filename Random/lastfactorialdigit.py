T = int(input())
A = [int(input()) for _ in range(T)]
d = {1:1, 2:2, 3:6, 4:4}
for N in A:
    if N>=5:
        print(0)
    else:
        print(d[N])