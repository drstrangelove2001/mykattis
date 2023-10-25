#not complete yet!

from math import ceil

S,N = map(int, input().split())
A = [0]*S
for i in input().split():
    ind = int(i)-1
    A[ind] = 1
    if ind != 0 and ind != S-1:
        A[ind-1] = A[ind+1] = 1
    elif ind == 0:
        A[1] = A[S-1] = 1
    else:
        A[S-2] = A[0] = 1
count = tmp = 0
for i in range(S):
    if A[i] == 0:
        tmp += 1
    else:
        count += 1 if tmp == 1 else ceil(tmp/2)
        tmp = 0
if A[0] == A[S-1] == 0:
    count -= 1
count += 1 if tmp == 1 else ceil(tmp/2)
print(count)


'''
0 1 2 1 0 0 1 2 1
'''