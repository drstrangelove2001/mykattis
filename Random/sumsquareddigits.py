P = int(input())
for _ in range(P):
    ans = 0
    K,b,n = map(int,input().split())
    while n>0:
        rem = n%b
        ans += rem**2
        n = n//b
    print(K, ans)