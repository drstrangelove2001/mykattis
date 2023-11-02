n = int(input())
trips = dict()
for _ in range(n):
    s,y = input().split()
    if s in trips:
        trips[s].append(int(y))
    else:
        trips[s] = [int(y)]
for key in trips:
    trips[key].sort()
q = int(input())
for _ in range(q):
    s,k = input().split()
    print(trips[s][int(k)-1])