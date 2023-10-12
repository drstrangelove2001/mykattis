P = int(input())
for _ in range(P):
    inp = list(map(int,input().split()))
    k,lst = inp[0],inp[1:]
    ans = 0
    for i in range(1,20):
        x = lst[i]
        j = i-1
        while j>=0:
            if lst[j] >= x:
                lst[j+1] = lst[j]
                ans += 1
            j-=1
        lst[j+1] = x
    print(k, ans)