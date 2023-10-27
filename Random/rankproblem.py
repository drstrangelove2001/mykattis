n,m = map(int, input().split())
A = [i for i in range(1,n+1)]
for _ in range(m):
    i,j = map(lambda x:int(x.strip('T')), input().split())
    indi,indj = A.index(i), A.index(j)
    if indi > indj:
        ele = A.pop(indj)
        A.insert(indi,ele)
print(' '.join([f'T{i}' for i in A]))