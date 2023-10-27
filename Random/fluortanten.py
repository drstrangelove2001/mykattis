#Partial points (32)

n = int(input())
A = list(map(int, input().split()))
A.pop(A.index(0))
sums = []
for i in range(n):
    A.insert(i,0)
    ans = 0
    for j,num in enumerate(A):
        ans += num*(j+1)
    sums.append(ans)
    A.pop(i)
print(max(sums))