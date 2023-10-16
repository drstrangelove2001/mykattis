n = int(input())
domdct = {}
kattisdct = {}
cons = 0
for _ in range(n):
    x = input()
    domdct[x] = 1 if x not in domdct else domdct[x] + 1
for _ in range(n):
    y = input()
    kattisdct[y] = 1 if y not in kattisdct else kattisdct[y] + 1
for key in domdct:
    if key in kattisdct:
        cons += min(domdct[key],kattisdct[key])
print(cons)