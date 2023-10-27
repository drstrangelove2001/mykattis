N,t = map(int, input().split())
A = list(map(int, input().split()))
if t==1:
    found = False
    compp = dict()
    for i in range(N):
        x = 7777 - A[i]
        if x in compp:
            found = True
            break
        compp[A[i]] = 7777 - A[i]
    print('Yes' if found else 'No')
elif t==2:
    print('Unique' if len(A) == len(set(A)) else 'Contains duplicate')
elif t==3:
    found = 0
    dup = dict()
    for i in range(N):
        if A[i] in dup:
            dup[A[i]] += 1
        else:
            dup[A[i]] = 1
    for key in dup:
        if dup[key] > N/2:
            found = key
            break
    print(found if found else -1)
elif t==4:
    tmp = sorted(A)
    if N%2==0:
        print(tmp[(N//2)-1], tmp[N//2])
    else:
        print(tmp[N//2])
elif t==5:
    tmp_lst = []
    for num in A:
        if 100<=num<=999:
            tmp_lst.append(num)
    tmp_lst.sort()
    print(' '.join(map(str, tmp_lst)))
