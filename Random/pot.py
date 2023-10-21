N = int(input())
A = [input() for _ in range(N)]
ans = 0
for num in A:
    ans += int(num[:-1])**int(num[-1])
print(ans)