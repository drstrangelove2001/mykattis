n,t = map(int, input().split())
potions = sorted([int(input()) for i in range(n)], reverse=True)
ans = [0]*n
for i in range(0,n):
    ans[i] = potions[i]
    ans[0:i] = [item-t if item-t>=0 else item for item in ans[0:i]]
print('YES'if all(ans) else'NO')


    
