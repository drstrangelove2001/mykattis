n = int(input())
r = input()
lst = [int(i) for i in r.split()]
regions = sorted(lst)
total = 0
for reg in regions[:(n//2)+1]:
    total += reg//2
total += sum(regions[(n//2)+1:])
print(total)
