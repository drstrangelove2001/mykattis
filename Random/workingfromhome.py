#not complete yet!

from math import ceil
m,p,n = map(int, input().split())
ep = 0
target = m
for _ in range(n):
    worked = int(input())
    if worked >= target:
        adjustment = worked - target
        ep += 1
        target = m - ceil((p/100)*adjustment)
    else:
        adjustment = target - worked
        target = m + ceil((p/100)*adjustment)
print(ep)