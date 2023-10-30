P,N = map(int, input().split())
ship = dict()
ans = 1
for i in range(1,N+1):
    part = input()
    if part not in ship:
        ship[part] = 1
    if len(ship.keys()) == P:
        print(i)
        P=0
if P:
    print('paradox avoided')