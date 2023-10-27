n = int(input())
A = list(map(int, input().split()))
k = 1
while True:
    tmp_lst = [A[i-1] for i in range(k,n+1,k)]
    l = len(tmp_lst)
    if l < 2:
        print('ABORT!')
        break
    for i in range(l-1):
        if tmp_lst[i] >= tmp_lst[i+1]:
            break
    if i==l-2 and tmp_lst[i] < tmp_lst[i+1]:
        print(k)
        break
    k+=1