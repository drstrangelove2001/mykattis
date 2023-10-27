L,H,K = map(int,input().split())
A = []
for i in range(H):
    row = []
    for j in range(L):
        row.append('_')
    A.append(row)
ch = 'a'
for _ in range(K):
    l,h,a,b = map(int, input().split())
    for i in range(b,b+h):
        for j in range(a,a+l):
            if i<H and j<L:
                A[i][j] = ch
    ch = chr(ord(ch) + 1)
[print(''.join(row)) for row in A]
