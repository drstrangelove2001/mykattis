import sys
n,m = map(int, sys.stdin.readline().split())
items = set(sys.stdin.readline().split())
for _ in range(n-1):
    shop = set(sys.stdin.readline().split())
    items = items & shop
print(len(items))
sl = sorted(list(items))
[print(i) for i in sl]