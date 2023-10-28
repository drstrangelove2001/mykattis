import heapq

k,n = map(int, input().split())
heap_of_mooses = []
Y,P = map(int, input().split())
heapq.heappush(heap_of_mooses, (Y,-P))
for _ in range(n+k-2):
    y,p = map(int, input().split())
    heapq.heappush(heap_of_mooses, (y,-p))

curr_year = 2011
tournament = []
won = False
for _ in range(k-1):
    y,p = heapq.heappop(heap_of_mooses)
    heapq.heappush(tournament, (p,y))
while curr_year < 2011 + n:
    y,p = heapq.heappop(heap_of_mooses)
    heapq.heappush(tournament, (p,y))
    if tournament[0][0] == -P:
        won = True
        break
    heapq.heappop(tournament)
    curr_year += 1
print(curr_year if won else 'unknown')