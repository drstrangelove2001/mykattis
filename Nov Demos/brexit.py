import sys
from collections import defaultdict, deque
C,P,X,L = map(int, sys.stdin.readline().split())
trade_unions = defaultdict(lambda: set())
sizes = dict()
for _ in range(P):
    a,b = map(int, sys.stdin.readline().split())
    trade_unions[a].add(b)
    trade_unions[b].add(a)
for i in range(1,C+1):
    sizes[i] = len(trade_unions[i])
stay = True
countries_to_leave = deque([L])
while countries_to_leave:
    leaving_country = countries_to_leave.popleft()
    if leaving_country == X:
        stay = False
        break
    for country in trade_unions[leaving_country]:
        trade_unions[country].discard(leaving_country)
        if len(trade_unions[country]) <= sizes[country]//2:
            countries_to_leave.append(country)
    trade_unions[leaving_country] = []
print('stay' if stay else 'leave')