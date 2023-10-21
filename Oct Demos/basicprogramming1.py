N,t = map(int,input().split())
A = [int(i) for i in input().split()]
if t == 1:
    print(7)
elif t==2:
    if A[0] > A[1]:
        print('Bigger')
    elif A[0] == A[1]:
        print('Equal')
    else:
        print('Smaller')
elif t==3:
    print(sorted(A[0:3])[1])
elif t==4:
    print(sum(A))
elif t==5:
    print(sum([item for item in A if item%2==0]))
elif t==6:
    lst = list(map(lambda x:chr((x%26)+97),A))
    print(''.join(lst))
else:
    i,count=0,0
    while i<N:
        count += 1
        i = A[i]
        if i == N-1:
            print('Done')
            break
        elif i>=N:
            print('Out')
            break
        if count > N:
            print('Cyclic')
            break
