from math import factorial as fact
n = int(input())
ans = sum([fact(n)//fact(n-k) for k in range(1,n+1)])
print(ans if ans<=10**9 else'JUST RUN!!')
