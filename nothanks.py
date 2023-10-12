n = int(input())
lst = sorted(list(map(int, input().split())))
ans = 0
for ind in range(0,n):
    if ind==0 or lst[ind] != lst[ind-1] + 1:
        ans += lst[ind]
print(ans)